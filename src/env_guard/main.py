import typer
from rich.console import Console
from rich.table import Table

from env_guard.scanner import scan_directory
from env_guard.checker import parse_env_example, check

app = typer.Typer()
console = Console()

@app.command()
def scan(
    path: str = typer.Argument(".", help="Path to the project directory to scan"),
    env_file: str = typer.Option(".env.example", "--env-file", "-e", help="Path to .env.example file"),
):
    """Scan a project directory for missing or unused environment variables."""
    console.print(f"\n[bold green]env-guard[/] scanning: [cyan]{path}[/]\n")

    # Scan .py files
    results = scan_directory(path)

    if not results:
        console.print("[yellow]No environment variable usage found.[/]")
        raise typer.Exit()

    # Show detected vars table
    table = Table(title="Detected Environment Variables", show_lines=True)
    table.add_column("File", style="cyan", no_wrap=True)
    table.add_column("Variable", style="bold white")
    table.add_column("Line", style="dim", justify="right")

    for file_path, vars_found in results.items():
        for var_name, line_num in vars_found:
            table.add_row(file_path, var_name, str(line_num))

    console.print(table)

    # Cross-reference against .env.example
    declared = parse_env_example(env_file)

    if not declared:
        console.print(f"[yellow]No .env.example found at '{env_file}' — skipping cross-reference.[/]\n")
        raise typer.Exit()

    missing, unused = check(results, declared)

    # Missing vars
    if missing:
        console.print("\n[bold red]Missing from .env.example:[/]")
        for var in missing:
            console.print(f"  [red]✗[/] {var}")
    else:
        console.print("\n[bold green]✓ No missing variables.[/]")

    # Unused vars
    if unused:
        console.print("\n[bold yellow]In .env.example but never used in code:[/]")
        for var in unused:
            console.print(f"  [yellow]⚠[/] {var}")
    else:
        console.print("[bold green]✓ No unused variables.[/]\n")