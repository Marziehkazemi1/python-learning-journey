import pandas as pd
import numpy as np

data = {
    "name": ["Ali", "Sara", "Reza", "Mina", "John"],
    "age": [25, -5, 30, 200, 22],
    "score": [85, 95, 120, 90, -10],
    "salary": [3000, 4500, np.nan, 4000, 3500]
}

df = pd.DataFrame(data)

invalid_age = df[
    (df["age"] < 18) |
    (df["age"] > 100)
]
print(invalid_age)

invalid_score = df[
    (df["score"] < 0) |
    (df["score"] > 100)
]
print(invalid_score)

print(df["age"].between(18, 100))

print(df[~df["age"].between(18, 100)])

data1 = {
    "age": ["25", "30", "unknown", "40", "invalid"],
    "salary": ["3000", "4500", "5000", "N/A", "3500"]
}
df1 = pd.DataFrame(data1)

#pd.to_numeric() :  Used to convert values ​​to numeric type.
# df1["age"] = pd.to_numeric(df1["age"])
df["age"] = pd.to_numeric(
    df["age"],
    errors="coerce"
)


df["age"] = df["age"].astype("int64")


data2 = {
    "date": [
        "2025-01-10",
        "2025-02-15",
        "2025-03-20"
    ]
}

df2 = pd.DataFrame(data2)
df2["date"] = pd.to_datetime(df2["date"])
print(df2.dtypes)


data3 = {
    "changes": [10, 15, -3, 8, 30],
    "complexity": [5, 8, 10, -2, 15],
    "lines": ["100", "150", "unknown", "80", "300"],
    "defect": [0, 1, 0, 1, 2]
}

df3 = pd.DataFrame(data3)
df3["lines"] = pd.to_numeric(
    df3["lines"],
    errors="coerce"
)

invalid_changes = df3[df3["changes"] < 0]

invalid_complexity = df3[df3["complexity"] < 0]

invalid_defect = df3[~df3["defect"].isin([0, 1])]


print(df.select_dtypes(include="number"))

