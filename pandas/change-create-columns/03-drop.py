import pandas as pd

data = {
    "changes": [10, 15, 20, 8, 30],
    "complexity": [5, 8, 10, 3, 15],
    "lines": [100, 150, 200, 80, 300],
    "defect": [0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

df = df.drop(columns="lines")   #delete column
df = df.drop(
    columns=["lines", "complexity"]
)

df = df.drop(index=2)   #delete row
df = df.drop(
    index=[1, 3]
)

df = df.drop(
    index=[1, 3],
    columns=["complexity", "lines"]
)

