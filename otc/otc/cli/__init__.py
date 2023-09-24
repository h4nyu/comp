import typer
import pandas as pd
from otc import EDA

app = typer.Typer()

@app.command()
def eda_command(file_path: str) -> None:
    """Run EDA on a file."""
    typer.echo(f"Running EDA on {file_path}.")
    df = pd.read_csv(file_path)
    eda = EDA()
    eda(df)

if __name__ == "__main__":
    app()
