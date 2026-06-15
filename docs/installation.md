# Installation

## Requirements

- Python 3.12 or higher

---

## With uv (Recommended)

[uv](https://github.com/astral-sh/uv) is the recommended way to install env-grep as a global CLI tool:

```bash
uv tool install env-grep
```

This installs env-grep in an isolated environment managed by uv, making both `env-grep` and `evg` available system-wide without touching your project's dependencies.

---

## With pip

Install inside a virtual environment:

```bash
pip install env-grep
```

!!! warning
    Avoid installing into your system Python directly. Always activate a virtual environment first.

---

## Verify the Installation

```bash
env-grep --help
evg scan --help
```

---

## Upgrading

```bash
# With uv
uv tool upgrade env-grep

# With pip
pip install --upgrade env-grep
```