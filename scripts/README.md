# Scripts

Utility scripts for project automation.

## daily_commit.py

A helper script for creating structured daily contributions.

### Usage

```bash
# Create a TIL (Today I Learned) entry
python daily_commit.py --type til --topic "Python decorators"

# Create a coding challenge solution
python daily_commit.py --type challenge --name "two-sum"

# Create a code snippet
python daily_commit.py --type snippet --topic "API helper" --lang python

# Create an experiment file
python daily_commit.py --type experiment --topic "FastAPI basics"

# Create without auto-commit
python daily_commit.py --type til --topic "Topic" --no-commit
```

### Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `--type` | `-t` | Content type: til, challenge, snippet, experiment |
| `--topic` | `-p` | Topic description |
| `--name` | `-n` | Name for challenges |
| `--lang` | `-l` | Language for snippets (default: python) |
| `--no-commit` | | Create file without committing |
| `--content` | `-c` | Optional content for TIL |

### Important Notes

1. This script creates **templates** - you must fill in real content
2. Never push template files without modification
3. Use `--no-commit` to edit before committing
4. The script is a helper, not a replacement for actual learning
