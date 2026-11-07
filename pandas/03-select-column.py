import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

#for select one column
print(df["state"])
#or
print("result:", df.state)

#For example, tell me how many rows with such and such columns
#first item in loc[] about count of row, second item about column
#this exm all of rows and colums of name "state"
print("loc:", df.loc[:, "state"])

#or we can give andis column
print("iloc:", df.iloc[:5, 1])