import pandas as pd
from pathlib import Path
import numpy as np

base_path = Path(__file__).parent
data_path = base_path / "data" / "students.csv"

dpath = Path("../data")

students = pd.read_csv(dpath / data_path)

col = 'prefer to study in'
students[col] = students[col].map({
    "Morning" : "M",
    "Anytime" : "A",
    "Night" : "N"
})
print("students[col]:", students[col])


col = "Height(CM)"
def transform_height(height):
    if height >= 170:
        return "tall"
    if 160 <= height <= 170:
        return 'medium'
    return 'short'

students[col] = students[col].map(transform_height)
print("student height:", students[col])
