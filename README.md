# env-grep

A command-line tool for Python projects that scans source files for environment variable usage and cross-references them against `.env.example` to surface missing or undocumented variables before they cause issues in production.

```bash
pip install env-grep
```

[![PyPI](https://img.shields.io/pypi/v/env-grep)](https://pypi.org/project/env-grep/)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![CI](https://github.com/ratherpixelate/env-grep/actions/workflows/tests.yml/badge.svg)](https://github.com/ratherpixelate/env-grep/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

Environment variable mismatches are a common source of production failures — a variable used in code but missing from the documented `.env.example`, or a stale entry in `.env.example` that no longer maps to anything in the codebase.

`env-grep` catches both classes of problem locally, before deployment, by statically scanning your Python source files and cross-referencing the results against your `.env.example`.

---

## Installation

```bash
pip install env-grep
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv add env-grep
```

---

## Usage

Run from the root of your Python project:

```bash
env-grep scan

# or using the short alias
evg scan
```

### Options

```
env-grep scan [OPTIONS] [PATH]

Arguments:
  PATH                   Directory to scan [default: .]

Options:
  -e, --env-file TEXT    Path to .env.example [default: .env.example]
  -i, --ignore TEXT      Name to exclude from scanning (repeatable)
      --no-table         Output plain text instead of a formatted table
      --help             Show this message and exit.
```

### Example Output

```
env-grep scanning: .

Ignoring: tests

                Detected Environment Variables
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━┓
┃ File               ┃ Variable      ┃ Line ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━┩
│ app/db.py          │ DATABASE_URL  │   12 │
│ app/payments.py    │ STRIPE_KEY    │    8 │
└────────────────────┴───────────────┴──────┘

Missing from .env.example:
  ✗ STRIPE_KEY

No unused variables.

Scan complete — 1 missing, 0 unused.
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

---

## Ignoring Files and Directories

Use `--ignore` or `-i` to exclude paths from scanning. The value is matched against each segment of every file path, so it applies at any depth.

```bash
# Ignore a directory
env-grep scan --ignore tests

# Ignore a specific file
env-grep scan --ignore legacy.py

# Ignore multiple paths
env-grep scan -i tests -i scripts -i migrations
```

---

## CI Integration

env-grep exits with code `1` if any variables are missing from `.env.example`, making it suitable for use in CI pipelines.

```yaml
- name: Check environment variables
  run: env-grep scan --no-table
```

Use `--no-table` for plain-text output that is easier to read in CI logs.

---

## How It Works

1. Recursively finds all `.py` files under the target directory, skipping common non-project paths (`.venv`, `__pycache__`, `.git`, `node_modules`, etc.) and any user-specified ignores.
2. Scans each file for environment variable access patterns using regex.
3. Parses `.env.example` to extract all declared variable names.
4. Computes the difference between variables used in code and variables declared in `.env.example`, reporting both missing and unused entries.

---

## Project Structure

```
env-grep/
├── src/
│   └── env_grep/
│       ├── __init__.py
│       ├── main.py        # CLI entrypoint (Typer)
│       ├── scanner.py     # Source file scanner
│       └── checker.py     # .env.example cross-reference logic
├── tests/
│   ├── test_scanner.py
│   ├── test_checker.py
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── pyproject.toml
└── README.md
```

---

## Contributing

Issues and pull requests are welcome. If you encounter a pattern that env-grep fails to detect, opening an issue with a minimal example is the most helpful way to report it.

---

## License

MIT © [ratherpixelate](https://github.com/ratherpixelate)