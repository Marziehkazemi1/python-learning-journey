import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

criterion1 = df['death'] > 50
print("criterion1:", criterion1)

criterion2 = (df["state"] == "WA") | (df["state"] == "AZ")
condition = criterion1 & criterion1
print("condition:", condition)
print("counts:", condition.value_counts())
print(df[condition])