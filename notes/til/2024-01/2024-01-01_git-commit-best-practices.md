# TIL: Git Commit Best Practices

**Date**: 2024-01-01
**Category**: Version Control

## What I Learned

Effective commit messages and practices that make version history useful and maintainable.

## Key Takeaways

- Use imperative mood in commit messages ("Add feature" not "Added feature")
- Keep subject line under 50 characters
- Separate subject from body with blank line
- Use body to explain what and why, not how

## Commit Message Format

```
type: short summary (50 chars max)

Longer description if needed. Wrap at 72 characters.
Explain the motivation for the change.

- Bullet points are okay
- Use present tense
```

## Semantic Commit Types

| Type | Description |
|------|-------------|
| feat | New feature |
| fix | Bug fix |
| docs | Documentation only |
| style | Formatting, no code change |
| refactor | Code restructuring |
| test | Adding tests |
| chore | Maintenance tasks |

## Resources

- [Conventional Commits](https://conventionalcommits.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

---
*Part of my daily learning journey in [daily-dev-lab](../../README.md)*
