from pathlib import Path


def parse_env_example(file_path: str) -> set[str]:
    """
    Parse a .env.example file and return a set of declared variable names.
    Skips blank lines and comments (lines starting with #).
    """
    path = Path(file_path)
    declared = set()

    if not path.exists():
        return declared

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Handle VAR=value, VAR=, and VAR (no equals)
        name = line.split("=")[0].strip()
        if name:
            declared.add(name)

    return declared


def check(
    scanned: dict[str, list[tuple[str, int]]],
    declared: set[str],
) -> tuple[list[str], list[str]]:
    """
    Compare scanned env vars against declared ones.

    Returns:
        missing: vars used in code but absent from .env.example
        unused:  vars in .env.example but never used in code
    """
    used = {var for vars_found in scanned.values() for var, _ in vars_found}

    missing = sorted(used - declared)
    unused = sorted(declared - used)

    return missing, unused