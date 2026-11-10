import pandas as pd
from pathlib import Path
import numpy as np

base_path = Path(__file__).parent
data_path = base_path / "data" / "all-states-history.csv"

dpath = Path("../data")

df = pd.read_csv(dpath / data_path)

#Here we changed the datetime type, which was a string, to the time type, and now we can perform time operations on it.
dt = pd.to_datetime(df['date'])
print('dt:', dt)
df = df.assign(date=dt)

print("year:", df['date'].dt.year)

df = df \
.assign(year = df["date"].dt.year) \
.assign(month = df["date"].dt.month) \
.assign(day = df["date"].dt.day) \
.assign(week = df["date"].dt.isocalendar().week) 
print("new df:", df)

df = df.set_index(['date'])
print(df)
print("2021 year:", df.loc['2021'].groupby(['state'])['hospitalized'].sum())   #return data label 2021