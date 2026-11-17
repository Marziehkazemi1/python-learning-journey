import pandas as pd

data = {
    "module": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "changes": [10, 15, 20, 8, 30, 12, 25, 18],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180],
    "defect": [0, 1, 0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

result = df.groupby("defect").filter(
    lambda x: len(x) >= 4
)

print(result)


print(df.groupby("defect").filter(
    lambda x: x["complexity"].mean() > 8
))

print(df.groupby("defect").filter(
    lambda x: x["lines"].sum() > 500
))

print(df.groupby("defect").filter(
    lambda x: (
        x["complexity"].mean() > 7
        and len(x) >= 4
    )
))

print(df.groupby(
    ["defect", "module"]
).filter(
    lambda x: len(x) >= 1
))