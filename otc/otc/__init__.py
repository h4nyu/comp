import pandas as pd
from typing import Optional
from matplotlib import pyplot as plt
from pathlib import Path


class EDA:
    def __init__(
        self,
    ) -> None:
        ...

    def __call__(
        self,
        df: pd.DataFrame,
        stock_ids: Optional[list[str]] = None,
        date_ids: Optional[list[str]] = None,
    ) -> None:
        if stock_ids:
            df = df[df["stock_id"].isin(stock_ids)]
        if date_ids:
            df = df[df["date_id"].isin(date_ids)]
        self.df = df
        print(df.iloc[0])
        # print(df[["seconds_in_bucket", "time_id"]].head())
        print(df.head())
        # for col in df.columns:
        #     print(f"------Column: {col} ------")
        #     print(df[col].describe())

        # columns = df.columns

    def save_graphs(
        self,
        path: str,
    ) -> None:
        if self.df is None:
            raise ValueError("Please call EDA class first.")
        Path(path).mkdir(parents=True, exist_ok=True)
        plot_dates = self.df["date_id"].unique()
        plot_stocks = self.df["stock_id"].unique()
        for date in plot_dates:
            for stock in plot_stocks:
                fig, axs = plt.subplots(6, 1, figsize=(10, 10))
                fig.suptitle(f"Stock: {stock}, Date: {date}")
                df = self.df[(self.df["date_id"] == date) & (self.df["stock_id"] == stock)]
                axs[0].plot(df["seconds_in_bucket"], df["target"])
                axs[0].set(ylabel="target")
                axs[1].plot(df["seconds_in_bucket"], df["bid_price"], label="bid_price")
                axs[1].plot(df["seconds_in_bucket"], df["ask_price"], label="ask_price")
                axs[1].plot(df["seconds_in_bucket"], df["wap"], label="wap")
                axs[1].plot(df["seconds_in_bucket"], df["reference_price"], label="reference_price")
                axs[1].set(ylabel="price")
                axs[1].legend()
                axs[2].plot(df["seconds_in_bucket"], df["imbalance_buy_sell_flag"], label="imbalance_buy_sell_flag")
                axs[3].plot(df["seconds_in_bucket"], df["ask_size"], label="ask_size")
                axs[3].plot(df["seconds_in_bucket"], df["bid_size"], label="bid_size")
                axs[3].set(ylabel="size")
                axs[3].legend()

                axs[4].plot(df["seconds_in_bucket"], df["far_price"], label="far_price")
                axs[4].plot(df["seconds_in_bucket"], df["near_price"], label="near_price")
                axs[4].legend()

                fig.savefig(f"{path}/{stock}_{date}.png")


        # plt.savefig(path)
