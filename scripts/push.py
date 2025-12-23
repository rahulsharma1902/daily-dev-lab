#!/usr/bin/env python3
"""
Git Push Helper - Uses token from .env for authentication
=========================================================

Usage:
    python push.py
    
This script allows pushing to GitHub even when another 
Git account is logged in on the system.
"""

import os
import subprocess
from pathlib import Path

# Load .env file
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass

PROJECT_ROOT = Path(__file__).parent.parent.resolve()


def push():
    """Push to GitHub using token from .env"""
    token = os.environ.get("GITHUB_TOKEN")
    username = os.environ.get("GITHUB_USERNAME")
    repo = os.environ.get("GITHUB_REPO", "daily-dev-lab")
    
    if not token or not username:
        print("❌ Error: GITHUB_TOKEN and GITHUB_USERNAME must be set in .env")
        return False
    
    # Build authenticated URL
    auth_url = f"https://{username}:{token}@github.com/{username}/{repo}.git"
    
    try:
        # Get current branch
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )
        branch = result.stdout.strip() or "main"
        
        print(f"📤 Pushing to {username}/{repo} ({branch})...")
        
        # Push
        subprocess.run(
            ["git", "push", auth_url, branch],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True
        )
        
        print("✅ Pushed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Push failed: {e}")
        return False


if __name__ == "__main__":
    push()
