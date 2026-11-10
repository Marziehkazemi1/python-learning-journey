import pandas as pd
from pathlib import Path
import numpy as np

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

#use groupby() when data split, apply, combin
print(df.groupby(['state'])['death'].sum().sort_values(ascending=False))

group = df.groupby(['state'])
print("group:", group)
print("groups:", group.groups)
print(group.groups.keys())
# print("AK:", group.get_group("AK"))

print(df.groupby(['state'])['death'].agg([np.sum, np.mean, np.amax]))