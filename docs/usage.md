# Usage

## Basic Scan

Run from the root of your Python project:

```bash
env-grep scan
```

env-grep will recursively scan all `.py` files, cross-reference the results against `.env.example`, and print a report.

---

## Options

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

---

## Scanning a Specific Directory

```bash
env-grep scan path/to/project
```

---

## Custom `.env.example` Path

```bash
env-grep scan --env-file config/.env.example
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

!!! note
    `--ignore tests` will match `tests/`, `src/tests/`, and any file named `tests.py` anywhere in the tree.

---

## CI Integration

env-grep exits with code `1` if any variables are missing from `.env.example`, making it suitable for CI pipelines.

```yaml
- name: Check environment variables
  run: env-grep scan --no-table
```

Use `--no-table` for plain-text output that is easier to read in CI logs.

---

## Example Output

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

## Known Limitations

- Variables accessed via dictionary unpacking (`**dotenv_values()`) are not detected.
- Variables passed through functions and accessed under a different name are not tracked across call boundaries.
- An empty `.env.example` is treated the same as a missing one — the cross-reference step is skipped in both cases.