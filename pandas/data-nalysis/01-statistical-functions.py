import pandas as pd
import numpy as np

data = {
    "changes": [10, 15, 20, 8, 30, 12, 25, 18],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180],
    "defect": [0, 1, 0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print(df["changes"].min())
print(df["lines"].max())
print(df["complexity"].mean())
print(df["changes"].median())
print(df["changes"].std())
print(df["lines"].sum())
print(df["complexity"].count())
print(df["changes"].quantile([0.25, 0.50, 0.75]))
