import pandas as pd
from pathlib import Path
import numpy as np

base_path = Path(__file__).parent
data_path = base_path / "data" / "iris.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

#minimum and maximum
print("min:", df["sepal.length"].min())
print("max:", df["sepal.length"].max())

#standard deviation
print("std:", df["petal.length"].std())

#remove row 7
print("remove 7:", df.drop(6, axis="index"))

#print information data frame
print("info:", df.info())

#print 5 rows first and 5 rows last
print("head:", df.head())
print("tail:", df.tail())

#print data type
print("data type:", df.dtypes)

#add column ===> sepal.length , sepal.width
gm = np.sqrt(df["sepal.length"] * df["sepal.width"])
df = df.assign(geometric_mean = gm)
print("geometric:", df)


total = ((df["petal.width"] < 1.5) * (df["variety"] == "Versicolor")).sum()
print("total:", total / len(df) * 100)
