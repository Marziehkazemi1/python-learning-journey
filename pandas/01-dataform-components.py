import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

print(df)

#for access index
print(df.index)

#for access column
print(df.columns)

#for access data
print(df.to_numpy())

print(issubclass(pd.RangeIndex, pd.Index))   #RangeIndex is a subclass of Index.
print(issubclass(df.columns.__class__, pd.Index))