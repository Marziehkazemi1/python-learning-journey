import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

#filter and select_dtypes  ==>  for select columns
#select_dtypes ===> for select columns base on data type
print("str:", df.select_dtypes(include="str"))     #return columns data type str
#also return array
print("int, str:", df.select_dtypes(include=["int", "str"]))    #return columns data type int and str
print("number:", df.select_dtypes(include="number"))  

#Which columns to ignore
print("exclude int:", df.select_dtypes(exclude="int"))    #return all columns Except for columns of int type


#filter
#items  ===> which columns select
#like   ===> It checks whether the name we wrote exists or not
print("filter items:", df.filter(items=["date", "state"]))
print("filter like:", df.filter(like="death"))
print("filter regex:", df.filter(regex=r"[nN]egative"))