#!/usr/bin/env python3
"""
Daily Auto Commit Script
========================

This script is designed to run automatically via Windows Task Scheduler.
It creates a daily TIL entry with the current date and pushes to GitHub.

IMPORTANT: This creates a REMINDER file - you should edit it with real content
during the day to make your commit meaningful.

Usage:
    python auto_daily.py              # Create today's TIL + commit + push
    python auto_daily.py --dry-run    # Preview without committing
"""

import os
import subprocess
import random
from datetime import datetime
from pathlib import Path

# Load .env file
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass

PROJECT_ROOT = Path(__file__).parent.parent.resolve()

# List of daily learning prompts/topics
DAILY_PROMPTS = [
    "Daily coding practice",
    "Algorithm review",
    "Code refactoring notes",
    "Learning log update",
    "Development notes",
    "Technical exploration",
    "Problem solving practice",
    "Code optimization notes",
    "Best practices review",
    "Documentation update",
]


def get_daily_topic():
    """Generate a topic for today."""
    today = datetime.now()
    day_name = today.strftime("%A")
    
    # Day-specific focuses
    day_topics = {
        "Monday": "Weekly kickoff - Goals and planning",
        "Tuesday": "Algorithm practice",
        "Wednesday": "Data structures review",
        "Thursday": "New technology exploration",
        "Friday": "Code review and refactoring",
        "Saturday": "Weekend project work",
        "Sunday": "Week review and learning summary",
    }
    
    return day_topics.get(day_name, random.choice(DAILY_PROMPTS))


def create_daily_entry():
    """Create today's learning entry."""
    today = datetime.now()
    month_dir = PROJECT_ROOT / "notes" / "til" / today.strftime("%Y-%m")
    month_dir.mkdir(parents=True, exist_ok=True)
    
    topic = get_daily_topic()
    filename = f"{today.strftime('%Y-%m-%d')}_{today.strftime('%A').lower()}.md"
    filepath = month_dir / filename
    
    # Skip if today's file already exists
    if filepath.exists():
        print(f"ℹ️  Today's entry already exists: {filepath}")
        return None
    
    template = f"""# TIL: {topic}

**Date**: {today.strftime('%Y-%m-%d')} ({today.strftime('%A')})
**Category**: Daily Practice

## What I Learned Today

<!-- 
📝 UPDATE THIS SECTION with what you actually learned today!
Delete this comment and add your real notes.
-->

- [ ] Add your first learning point here
- [ ] Add another insight
- [ ] Any code snippets or examples?

## Key Takeaways

1. **Main insight**: Describe your key learning
2. **Practical application**: How can you use this?

## Code Example (if applicable)

```python
# Add any code you wrote or learned about today
pass
```

## Tomorrow's Focus

- [ ] What do you want to learn next?

---
*Part of my daily learning journey in [daily-dev-lab](../../README.md)*
*Generated on {today.strftime('%Y-%m-%d %H:%M')} - Remember to update with real content!*
"""
    
    filepath.write_text(template, encoding='utf-8')
    print(f"✅ Created: {filepath}")
    return str(filepath)


def git_commit_and_push(filepath: str, topic: str):
    """Commit and push the file."""
    token = os.environ.get("GITHUB_TOKEN")
    username = os.environ.get("GITHUB_USERNAME")
    repo = os.environ.get("GITHUB_REPO", "daily-dev-lab")
    
    try:
        # Stage
        subprocess.run(
            ["git", "add", filepath],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True
        )
        
        # Commit
        today = datetime.now().strftime("%Y-%m-%d")
        commit_msg = f"📝 daily: {today} - {topic}"
        
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True
        )
        print(f"✅ Committed: {commit_msg}")
        
        # Push if credentials available
        if token and username:
            auth_url = f"https://{username}:{token}@github.com/{username}/{repo}.git"
            
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True
            )
            branch = result.stdout.strip() or "main"
            
            subprocess.run(
                ["git", "push", auth_url, branch],
                cwd=PROJECT_ROOT,
                check=True,
                capture_output=True
            )
            print("✅ Pushed to GitHub!")
        else:
            print("⚠️  No token found - committed locally only")
            
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        return False


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Daily Auto Commit")
    parser.add_argument("--dry-run", action="store_true", help="Preview without committing")
    args = parser.parse_args()
    
    print(f"\n🌅 Daily Dev Lab - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)
    
    topic = get_daily_topic()
    print(f"📋 Today's focus: {topic}\n")
    
    if args.dry_run:
        print("🔍 Dry run mode - no files created")
        return 0
    
    filepath = create_daily_entry()
    
    if filepath:
        git_commit_and_push(filepath, topic)
        print("\n💡 Remember to update the file with your actual learnings!")
    
    return 0


if __name__ == "__main__":
    exit(main())
