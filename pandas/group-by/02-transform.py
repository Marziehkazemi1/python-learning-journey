import pandas as pd
#It performs a calculation on each group, but unlike agg(), it returns the result as the number of rows in the original dataframe.

data = {
    "module": ["A", "B", "C", "D", "E", "F"],
    "complexity": [5, 8, 10, 3, 15, 6],
    "defect": [0, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

print(df.groupby("defect")["complexity"].agg("mean"))

df["group_mean"] = (
    df.groupby("defect")["complexity"]
    .transform("mean")
)
print(df)

df["complexity_normalized"] = (
    df["complexity"].transform(
        lambda x: x / x.max()
    )
)


print(df.groupby("defect")["complexity"].transform("sum"))
print(df.groupby("defect")["complexity"].transform("median"))

df[["changes", "complexity", "lines"]].transform(
    lambda x: x / x.max()
)

df["difference"] = (
    df["complexity"] -
    df.groupby("defect")["complexity"].transform("mean")
)

df["changes_scaled"] = (
    df["changes"].transform(
        lambda x: x / x.max()
    )
)

df["group_zscore"] = (
    df.groupby("defect")["complexity"]
    .transform(
        lambda x: (x - x.mean()) / x.std()
    )
)