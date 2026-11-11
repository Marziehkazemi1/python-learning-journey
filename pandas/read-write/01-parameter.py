import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path.parent / "data" / "students.csv"

students = pd.read_csv(
    data_path,
    header=None,
    names=["id", "name", "age", "score"]   #name of clumns 
)

print(students)

#sep: What character separates the values ​​in the file
students = pd.read_csv(
    data_path,
    sep=";"
)

print(students)

#usecols: Which columns to read from the file
students = pd.read_csv(
    data_path,
    usecols=["Gender", "Department"]
)

print(students)

students = pd.read_csv(
    data_path,
    usecols=[0, 2, 3]
)
print(students)

students = pd.read_csv(
    data_path,
    usecols=lambda column: column in ["Gender", "Department"]
)
print(students)


students = pd.read_csv(
    data_path,
    header=1,
    # index_col="Gender",
    sep=",",
    # usecols=[ "Department", "Height(CM)"]
)

print(students)