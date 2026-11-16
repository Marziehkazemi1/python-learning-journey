import pandas as pd

data = {
    "changes": [10, 15, 20, 8, 30, 12, 25, 18],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180],
    "defect": [0, 1, 0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print(df["defect"].value_counts())
print(df["defect"].value_counts(ascending=True))
print(df["defect"].value_counts(normalize=True) * 100)
print(df["defect"].value_counts(dropna=False))

