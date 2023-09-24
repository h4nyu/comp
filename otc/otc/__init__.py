import pandas as pd


class EDA:
    def __init__(
        self,
    ) -> None:
        ...

    def __call__(self, df: pd.DataFrame) -> None:
        columns = df.columns
        print(columns)
        ...
