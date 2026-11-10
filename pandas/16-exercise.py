import pandas as pd
from pathlib import Path
import numpy as np

base_path = Path(__file__).parent
data_path = base_path / "data" / "students.csv"

dpath = Path("../data")

students = pd.read_csv(dpath / data_path)

students['is_male'] = 1
students.loc[students["Gender"] == "Female", "is_male"] = 0

print("is male:", students['is_male'])

conditions = [
    (students["college mark"] < 50),
    (students["college mark"] >= 50) & (students["college mark"] < 60),
    (students["college mark"] >= 60) & (students["college mark"] < 70),
    (students["college mark"] >= 70) & (students["college mark"] < 80),
    (students["college mark"] >= 80) 
]

values = [
    "F",
    "D",
    "C",
    "B",
    "A"
]

students["college_score"] = np.select(
    conditions,
    values,
    default="Unknown"
)
print("collage score:", students['college_score'])