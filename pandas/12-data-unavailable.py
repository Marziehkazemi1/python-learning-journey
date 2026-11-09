import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

#check the value is Nun or not
print("isna:", df.isna().sum())

#It can fill the NaN quantities with the amount we give it. not change original data frame and create one copy 
print("fillna:", df.fillna(0))

#we can delete row or column
#how  ==>  What strategy should be used to delete that row or column
col_names = ["death", "totalTestsAntibody"]
print("any:", df[col_names].dropna(how="any"))
print("all:", df[col_names].dropna(how="all"))
