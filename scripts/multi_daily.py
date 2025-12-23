#!/usr/bin/env python3
"""
Multi-Commit Daily Script
=========================

Creates multiple commits throughout the day with different content types.
Designed to run via Windows Task Scheduler at different times.

Usage:
    python multi_daily.py --slot morning
    python multi_daily.py --slot midday
    python multi_daily.py --slot afternoon
    python multi_daily.py --slot evening
    python multi_daily.py --slot night
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

# Different content for different time slots
SLOT_CONFIG = {
    "morning": {
        "type": "til",
        "folder": "notes/til",
        "topics": [
            "Morning coding warmup",
            "Daily learning kickoff",
            "Code review notes",
            "Morning problem solving",
        ],
        "emoji": "🌅"
    },
    "midday": {
        "type": "challenge",
        "folder": "challenges",
        "topics": [
            "Algorithm practice",
            "Data structure drill",
            "Coding challenge",
            "Problem solving session",
        ],
        "emoji": "🧩"
    },
    "afternoon": {
        "type": "snippet",
        "folder": "snippets/python",
        "topics": [
            "Utility function",
            "Helper method",
            "Code pattern",
            "Reusable component",
        ],
        "emoji": "✂️"
    },
    "evening": {
        "type": "experiment",
        "folder": "experiments/python",
        "topics": [
            "New library exploration",
            "Technology spike",
            "Concept testing",
            "Feature prototype",
        ],
        "emoji": "🔬"
    },
    "night": {
        "type": "notes",
        "folder": "notes/til",
        "topics": [
            "Day summary",
            "Learning reflection",
            "Progress notes",
            "End of day review",
        ],
        "emoji": "🌙"
    },
}


def create_content(slot: str) -> tuple:
    """Create content for the given time slot."""
    config = SLOT_CONFIG.get(slot, SLOT_CONFIG["morning"])
    today = datetime.now()
    topic = random.choice(config["topics"])
    
    # Create folder
    if config["type"] == "til" or config["type"] == "notes":
        folder = PROJECT_ROOT / "notes" / "til" / today.strftime("%Y-%m")
    elif config["type"] == "challenge":
        folder = PROJECT_ROOT / "challenges" / today.strftime("%Y-%m")
    elif config["type"] == "snippet":
        folder = PROJECT_ROOT / "snippets" / "python"
    else:
        folder = PROJECT_ROOT / "experiments" / "python"
    
    folder.mkdir(parents=True, exist_ok=True)
    
    # Generate unique filename with timestamp
    timestamp = today.strftime("%H%M")
    date_str = today.strftime("%Y-%m-%d")
    
    if config["type"] in ["til", "notes"]:
        filename = f"{date_str}_{slot}_{timestamp}.md"
        content = f"""# {topic}

**Date**: {today.strftime('%Y-%m-%d %H:%M')}
**Session**: {slot.title()}

## Notes

- Learning point 1
- Learning point 2
- Key insight

## Code Reference

```python
# Code snippet or example
pass
```

---
*{slot.title()} session - Daily Dev Lab*
"""
    elif config["type"] == "challenge":
        filename = f"{today.strftime('%d')}_{slot}_{timestamp}.py"
        content = f'''"""
{topic}
Date: {today.strftime('%Y-%m-%d %H:%M')}
Session: {slot.title()}

Problem: [Description]
Approach: [Your approach]
Complexity: O(?)
"""

def solution():
    """Solution implementation."""
    # TODO: Your solution
    pass

if __name__ == "__main__":
    print(solution())
'''
    elif config["type"] == "snippet":
        filename = f"{slot}_{timestamp}_{date_str.replace('-', '')}.py"
        content = f'''"""
{topic}
Created: {today.strftime('%Y-%m-%d %H:%M')}
"""

def helper():
    """Helper function."""
    # TODO: Implementation
    pass

if __name__ == "__main__":
    helper()
'''
    else:  # experiment
        filename = f"{today.strftime('%Y%m%d')}_{slot}_{timestamp}.py"
        content = f'''"""
{topic}
Date: {today.strftime('%Y-%m-%d %H:%M')}
Session: {slot.title()}

Objective: [What to explore]
Result: [What was learned]
"""

def experiment():
    """Experiment code."""
    print("Running {slot} experiment...")
    # TODO: Experimental code
    pass

if __name__ == "__main__":
    experiment()
'''
    
    filepath = folder / filename
    filepath.write_text(content, encoding='utf-8')
    
    return str(filepath), topic, config["emoji"]


def git_commit_push(filepath: str, topic: str, emoji: str, slot: str):
    """Commit and push."""
    token = os.environ.get("GITHUB_TOKEN")
    username = os.environ.get("GITHUB_USERNAME")
    repo = os.environ.get("GITHUB_REPO", "daily-dev-lab")
    
    try:
        subprocess.run(["git", "add", filepath], cwd=PROJECT_ROOT, check=True, capture_output=True)
        
        commit_msg = f"{emoji} {slot}: {topic}"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=PROJECT_ROOT, check=True, capture_output=True)
        print(f"✅ Committed: {commit_msg}")
        
        if token and username:
            auth_url = f"https://{username}:{token}@github.com/{username}/{repo}.git"
            result = subprocess.run(["git", "branch", "--show-current"], cwd=PROJECT_ROOT, capture_output=True, text=True)
            branch = result.stdout.strip() or "main"
            subprocess.run(["git", "push", auth_url, branch], cwd=PROJECT_ROOT, check=True, capture_output=True)
            print("✅ Pushed to GitHub!")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        return False


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--slot", choices=["morning", "midday", "afternoon", "evening", "night"], required=True)
    args = parser.parse_args()
    
    print(f"\n🕐 Daily Dev Lab - {args.slot.upper()} Session")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)
    
    filepath, topic, emoji = create_content(args.slot)
    print(f"✅ Created: {filepath}")
    
    git_commit_push(filepath, topic, emoji, args.slot)
    
    return 0


if __name__ == "__main__":
    exit(main())
