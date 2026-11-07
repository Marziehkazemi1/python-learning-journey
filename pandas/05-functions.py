import pandas as pd
from pathlib import Path

base_path = Path(__file__).resolve().parent
data_path = base_path / "data" / "all-states-history.csv"
dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

print("shape:", df.shape)
print("len:", len(df))   #show count of rows
print("size:", df["state"].size)

print("value count:", df["state"].value_counts())    #for show count of columns
print("normalize:", df["state"].value_counts(normalize=True))   #we can normalize data between 0 , 1

print("count:", df["totalTestsViral"].count())    #Give the number of columns that are not NaN
print("min:", df["totalTestsViral"].min())
print("max:", df["totalTestsViral"].max())
print("mean:", df["totalTestsViral"].mean())
print("describe:", df["totalTestsViral"].describe())
print("quantile:", df["totalTestsViral"].quantile([0.1, 0.2, 0.5]))
