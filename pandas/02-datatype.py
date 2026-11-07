import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

#Shows the first 5 lines of the dataframe.
print("head:", df.head())

#Shows the last 5 lines of the dataframe.
print("tail:", df.tail())

#data type for each column  
#if show object means this data is string 
print("dtypes:", df.dtypes)

#for show count of columns
print("value counts:", df.dtypes.value_counts())

#for show summary dataframe
print("info:", df.info())
