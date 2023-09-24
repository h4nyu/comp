import typer
import pandas as pd
from otc import EDA
from typing import Optional

app = typer.Typer()


@app.command()
def eda_command(
    file_path: str,
    stock_ids: Optional[list[int]] = typer.Option(
        default=None,
    ),
    date_ids: Optional[list[int]] = typer.Option(default=None),
    output_dir: str = typer.Option(default="output"),

) -> None:
    """Run EDA on a file."""
    df = pd.read_csv(file_path)
    eda = EDA()
    typer.echo(f"stock_ids: {stock_ids}")
    eda(
        df,
        stock_ids=stock_ids,
        date_ids=date_ids,
    )
    eda.save_graphs(output_dir)


if __name__ == "__main__":
    app()
