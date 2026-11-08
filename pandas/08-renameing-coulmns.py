import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

#rename not change original data frame and return new data frame
print(
    df.rename(columns={
    "deathConfirmed" : "death_confirmed",
    "deathIncrease" : "death_increase"
}).columns
)

#set_index()  ==> which coulmn select for index
print(
    "index:",
    df.set_index("state").rename(index={"AK": "Alaska"})
)

#we can return a function to each columns
def upper(value):
    return value.upper()

print("upper:", df.rename(columns=upper).columns)    #all of columns upper