import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

print(df["death"] + 1)

print(df["death"] / df["death"].max())  # df["death"].div(df["death"].max())

print(df["death"] >= 100)   # df["death"].ge(100)

print(df["state"] == "WA")  # df["state"].eq("WA")