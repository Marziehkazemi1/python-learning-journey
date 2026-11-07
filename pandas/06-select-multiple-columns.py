import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

print(df[["state", "death"]])
print("loc:", df.loc[3:5, ["state", "death"]])   #Returns columns "state", "death" 3 to 5.
print("iloc:", df.iloc[:5, [0, 5]])    #give columns 0 and 5
