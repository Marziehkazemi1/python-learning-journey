import pandas as pd

data = {
    "changes": [10, 15, 20, 8, 30, 12, 25, 18],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180],
    "defects": [0, 1, 1, 0, 1, 0, 1, 1]
}
df = pd.DataFrame(data)
print(df)

result = df[df["complexity"] > 10]
print(result)

print(df[df["complexity"] < 10])

print(df[df["lines"] >= 200])

print(df[df["defects"] == 1])

result = df[
    (df["complexity"] > 10) &
    (df["lines"] > 200)
]
print(result)


result = df[
    (df["complexity"] > 12) |
    (df["changes"] > 50)
]
print(result)

print(df[~(df["defects"] == 1)])


result = df[
    (df["complexity"] > 10) &
    (
        (df["lines"] > 200) |
        (df["changes"] > 20)
    )
]
print(result)
