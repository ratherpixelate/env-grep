import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def scan(
    path: str = typer.Argument(".", help="Path to the project directory to scan"),
):
    """Scan a project directory for missing or unused environment variables."""
    console.print(f"[bold green]env-guard[/] scanning: [cyan]{path}[/]")

if __name__ == "__main__":
    app()