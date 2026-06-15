# Contributing

Contributions are welcome. This page covers how to set up the project locally and run the test suite.

---

## Setup

```bash
git clone https://github.com/ratherpixelate/env-grep.git
cd env-grep
uv sync
```

---

## Running Tests

```bash
uv run pytest tests/ -v
```

The test suite covers the scanner, checker, and CLI entrypoint across 31 tests. All tests must pass before opening a pull request.

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
├── docs/
├── mkdocs.yml
├── pyproject.toml
└── README.md
```

---

## Reporting Issues

If you encounter a pattern that env-grep fails to detect, opening an issue with a minimal reproducible example is the most helpful way to report it.

[Open an issue →](https://github.com/ratherpixelate/env-grep/issues)