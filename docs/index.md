# env-grep

A command-line tool for Python projects that scans source files for environment variable usage and cross-references them against `.env.example` to surface missing or undocumented variables before they cause issues in production.

```bash
uv tool install env-grep
```

---

## Why env-grep?

Environment variable mismatches are a common source of production failures. A variable used in code but absent from `.env.example` means the next developer to clone the repo will have no way of knowing it needs to be set — until something breaks.

env-grep catches both classes of problem locally, before deployment:

- **Missing** — variables used in code but not documented in `.env.example`
- **Unused** — variables in `.env.example` that are never referenced in code

---

## Quick Start

```bash
# Install
uv tool install env-grep

# Run from your project root
env-grep scan

# Or use the short alias
evg scan
```

---

## What Gets Detected

env-grep scans for the following patterns across all `.py` files in your project:

**Standard `os` module usage**
```python
os.getenv("DATABASE_URL")
os.environ["DATABASE_URL"]
os.environ.get("DATABASE_URL")
```

**`python-dotenv` usage via `dotenv_values()`**
```python
config = dotenv_values(".env")
config["DATABASE_URL"]
config.get("DATABASE_URL")
```