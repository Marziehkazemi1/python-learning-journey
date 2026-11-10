import pandas as pd
from pathlib import Path

#use drop() for delete column or row data frame

base_path = Path(__file__).parent
data_path = base_path / "data" / "students.csv"

dpath = Path("../data")

students = pd.read_csv(dpath / data_path)

X = students.drop("Gender", axis="columns")
Y = students["Gender"]
print("x head:", X.head())
print("y head:", Y.head())
