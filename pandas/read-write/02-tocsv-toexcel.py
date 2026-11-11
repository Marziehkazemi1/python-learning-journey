import pandas as pd
from pathlib import Path

base_path = Path(__file__).resolve().parent

data_path = base_path / "data" / "students.csv"

students = pd.read_csv(data_path)

output_path = base_path.parent / "data" / "new_students.csv"

students.to_csv(
    output_path,
    index=False,
    columns=["name", "age"],
    encoding="utf-8"
)


output_excel = base_path.parent / "data" / "students.xlsx"

students.to_excel(
    output_excel,
    index=False,
    sheet_name="Students"
)