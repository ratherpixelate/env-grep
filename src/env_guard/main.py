import typer
from rich.console import Console
from rich.table import Table

from env_guard.scanner import scan_directory

app = typer.Typer()
console = Console()

@app.command()
def scan(
    path: str = typer.Argument(".", help="Path to the project directory to scan"),
):
    """Scan a project directory for missing or unused environment variables."""
    console.print(f"\n[bold green]env-guard[/] scanning: [cyan]{path}[/]\n")

    results = scan_directory(path)

    if not results:
        console.print("[yellow]No environment variable usage found.[/]")
        raise typer.Exit()

    table = Table(title="Detected Environment Variables", show_lines=True)
    table.add_column("File", style="cyan", no_wrap=True)
    table.add_column("Variable", style="bold white")
    table.add_column("Line", style="dim", justify="right")

    for file_path, vars_found in results.items():
        for var_name, line_num in vars_found:
            table.add_row(file_path, var_name, str(line_num))

    console.print(table)

if __name__ == "__main__":
    app()