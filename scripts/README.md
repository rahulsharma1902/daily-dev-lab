# Scripts

Utility scripts for project automation.

## daily_commit.py

A helper script for creating structured daily contributions with optional auto-push.

### Setup for Auto-Push

1. Copy `.env.example` to `.env` in the project root
2. Add your GitHub Personal Access Token (generate at https://github.com/settings/tokens)
3. Set your username and repo name

```env
GITHUB_TOKEN=your_token_here
GITHUB_USERNAME=rahulsharma1902
GITHUB_REPO=daily-dev-lab
```

4. Install python-dotenv (optional but recommended):
```bash
pip install python-dotenv
```

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

# Create, commit, AND push to GitHub (uses token from .env)
python daily_commit.py --type til --topic "Topic" --push
```

### Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `--type` | `-t` | Content type: til, challenge, snippet, experiment |
| `--topic` | `-p` | Topic description |
| `--name` | `-n` | Name for challenges |
| `--lang` | `-l` | Language for snippets (default: python) |
| `--no-commit` | | Create file without committing |
| `--push` | | Push to GitHub after commit (uses GITHUB_TOKEN) |
| `--content` | `-c` | Optional content for TIL |

### Important Notes

1. This script creates **templates** - you must fill in real content
2. Never push template files without modification
3. Use `--no-commit` to edit before committing
4. The `--push` flag requires `.env` with valid GITHUB_TOKEN
5. The script is a helper, not a replacement for actual learning

