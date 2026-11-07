import pandas as pd
from pathlib import Path

base_path = Path(__file__).resolve().parent

data_path = base_path / "data" / "all-states-history.csv"

df = pd.read_csv(data_path)

print(df.head())

# Write CSV data to Excel
excel_path = base_path / "data" / "all-states-history.xlsx"

df.to_excel(
    excel_path,
    sheet_name="covid",
    index=False
)

# Read Excel file
df = pd.read_excel(
    excel_path,
    sheet_name="covid"
)

print(df.head())