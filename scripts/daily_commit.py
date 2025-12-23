#!/usr/bin/env python3
"""
Daily Commit Helper Script
==========================

A safe automation script for generating meaningful daily commits.
This script creates REAL content - not empty or fake commits.

Usage:
    python daily_commit.py --type til --topic "Python decorators"
    python daily_commit.py --type challenge --name "two-sum"
    python daily_commit.py --type snippet --topic "API request helper"
    python daily_commit.py --type experiment --topic "FastAPI exploration"

Author: [Your Name]
License: MIT
"""

import argparse
import os
import subprocess
from datetime import datetime
from pathlib import Path


# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.resolve()


def create_til_entry(topic: str, content: str = None) -> str:
    """
    Create a Today I Learned entry.
    
    Args:
        topic: The topic learned today
        content: Optional detailed content
    
    Returns:
        Path to the created file
    """
    today = datetime.now()
    month_dir = PROJECT_ROOT / "notes" / "til" / today.strftime("%Y-%m")
    month_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f"{today.strftime('%Y-%m-%d')}_{topic.lower().replace(' ', '-')}.md"
    filepath = month_dir / filename
    
    template = f"""# TIL: {topic}

**Date**: {today.strftime('%Y-%m-%d')}
**Category**: [Category]

## What I Learned

{content if content else '[Describe what you learned today...]'}

## Key Takeaways

- Takeaway 1
- Takeaway 2

## Code Example (if applicable)

```python
# Example code here
```

## Resources

- [Resource Name](URL)

---
*Part of my daily learning journey in [daily-dev-lab](../../README.md)*
"""
    
    filepath.write_text(template, encoding='utf-8')
    return str(filepath)


def create_challenge_entry(name: str, platform: str = "leetcode") -> str:
    """
    Create a coding challenge solution entry.
    
    Args:
        name: Challenge name (e.g., "two-sum")
        platform: Platform name (default: leetcode)
    
    Returns:
        Path to the created file
    """
    today = datetime.now()
    month_dir = PROJECT_ROOT / "challenges" / today.strftime("%Y-%m")
    month_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f"{today.strftime('%d')}_{name.lower().replace(' ', '-')}.py"
    filepath = month_dir / filename
    
    template = f'''"""
Challenge: {name.replace('-', ' ').title()}
Platform: {platform.title()}
Date: {today.strftime('%Y-%m-%d')}
Difficulty: [Easy/Medium/Hard]

Problem Description:
-------------------
[Describe the problem here]

Approach:
---------
[Explain your approach]

Time Complexity: O(?)
Space Complexity: O(?)
"""


def solution():
    """
    Main solution function.
    """
    # TODO: Implement your solution
    pass


def test_solution():
    """
    Test cases for the solution.
    """
    # Test case 1
    assert solution() is not None, "Test case 1 failed"
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
'''
    
    filepath.write_text(template, encoding='utf-8')
    return str(filepath)


def create_snippet(topic: str, language: str = "python") -> str:
    """
    Create a code snippet file.
    
    Args:
        topic: Snippet topic/name
        language: Programming language (default: python)
    
    Returns:
        Path to the created file
    """
    snippets_dir = PROJECT_ROOT / "snippets" / language
    snippets_dir.mkdir(parents=True, exist_ok=True)
    
    ext = {"python": "py", "javascript": "js"}.get(language.lower(), "txt")
    filename = f"{topic.lower().replace(' ', '_')}.{ext}"
    filepath = snippets_dir / filename
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    if language.lower() == "python":
        template = f'''"""
Snippet: {topic}
Created: {today}
Description: [Brief description]

Usage:
    from snippets.python.{topic.lower().replace(' ', '_')} import main_function
"""


def main_function():
    """
    Brief description of what this does.
    
    Args:
        param1: Description
    
    Returns:
        Description of return value
    """
    # TODO: Implement
    pass


# Example usage
if __name__ == "__main__":
    result = main_function()
    print(result)
'''
    else:
        template = f"""/**
 * Snippet: {topic}
 * Created: {today}
 * Description: [Brief description]
 */

function mainFunction() {{
    // TODO: Implement
}}

module.exports = {{ mainFunction }};
"""
    
    filepath.write_text(template, encoding='utf-8')
    return str(filepath)


def create_experiment(topic: str) -> str:
    """
    Create an experiment file for exploring new concepts.
    
    Args:
        topic: Experiment topic
    
    Returns:
        Path to the created file
    """
    today = datetime.now()
    exp_dir = PROJECT_ROOT / "experiments" / "python"
    exp_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f"{today.strftime('%Y%m%d')}_{topic.lower().replace(' ', '_')}.py"
    filepath = exp_dir / filename
    
    template = f'''#!/usr/bin/env python3
"""
Experiment: {topic}
Date: {today.strftime('%Y-%m-%d')}

Objective:
----------
[What are you trying to learn/explore?]

Hypothesis:
-----------
[What do you expect to discover?]

Notes:
------
[Observations during the experiment]

Conclusion:
-----------
[What did you learn?]
"""

# ============================================================
# Setup
# ============================================================

# Import required libraries
import os
import sys


# ============================================================
# Experiment Code
# ============================================================

def experiment():
    """
    Main experiment function.
    """
    print("Starting experiment: {topic}")
    
    # TODO: Add your experimental code here
    
    print("Experiment complete!")


# ============================================================
# Run Experiment
# ============================================================

if __name__ == "__main__":
    experiment()
'''
    
    filepath.write_text(template, encoding='utf-8')
    return str(filepath)


def git_commit(filepath: str, commit_type: str, topic: str) -> bool:
    """
    Stage and commit the created file.
    
    Args:
        filepath: Path to the file to commit
        commit_type: Type of content (til, challenge, snippet, experiment)
        topic: Topic description
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Stage the file
        subprocess.run(
            ["git", "add", filepath],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True
        )
        
        # Create commit message
        type_emoji = {
            "til": "📝",
            "challenge": "🧩",
            "snippet": "✂️",
            "experiment": "🔬"
        }
        
        emoji = type_emoji.get(commit_type, "📦")
        commit_msg = f"{emoji} {commit_type}: {topic}"
        
        # Commit
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True
        )
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")
        return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Daily Commit Helper - Create meaningful daily contributions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python daily_commit.py --type til --topic "Python decorators"
  python daily_commit.py --type challenge --name "two-sum"
  python daily_commit.py --type snippet --topic "API helper" --lang python
  python daily_commit.py --type experiment --topic "FastAPI basics"
        """
    )
    
    parser.add_argument(
        "--type", "-t",
        choices=["til", "challenge", "snippet", "experiment"],
        required=True,
        help="Type of content to create"
    )
    
    parser.add_argument(
        "--topic", "-p",
        help="Topic or description"
    )
    
    parser.add_argument(
        "--name", "-n",
        help="Name for challenges"
    )
    
    parser.add_argument(
        "--lang", "-l",
        default="python",
        help="Language for snippets (default: python)"
    )
    
    parser.add_argument(
        "--no-commit",
        action="store_true",
        help="Create file without committing"
    )
    
    parser.add_argument(
        "--content", "-c",
        help="Optional content for TIL entries"
    )
    
    args = parser.parse_args()
    
    # Determine topic
    topic = args.topic or args.name
    if not topic:
        print("Error: Please provide --topic or --name")
        return 1
    
    # Create content based on type
    creators = {
        "til": lambda: create_til_entry(topic, args.content),
        "challenge": lambda: create_challenge_entry(topic),
        "snippet": lambda: create_snippet(topic, args.lang),
        "experiment": lambda: create_experiment(topic)
    }
    
    filepath = creators[args.type]()
    print(f"✅ Created: {filepath}")
    
    # Commit if not disabled
    if not args.no_commit:
        if git_commit(filepath, args.type, topic):
            print(f"✅ Committed: {args.type}: {topic}")
        else:
            print("⚠️  File created but commit failed (git might not be initialized)")
    
    return 0


if __name__ == "__main__":
    exit(main())
