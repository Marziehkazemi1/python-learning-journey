import pandas as pd
import numpy as np

data = {
    "changes": [10, 15, 20, 8, 30],
    "complexity": [5, 8, 10, 3, 15],
    "lines": [100, 150, 200, 80, 300],
    "defect": [0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

df["total"] = df["changes"] + df["complexity"]   #create new column
df["change_ratio"] = df["changes"] / df["lines"]

df["complexity_level"] = "Low"
df.loc[df["complexity"] > 10, "complexity_level"] = "High"

#np.where(condition, value_if_true, value_if_false)
df["complexity_level"] = np.where(
    df["complexity"] > 10,
    "High",
    "Low"
)


conditions = [
    df["complexity"] <= 5,
    (df["complexity"] > 5) & (df["complexity"] <= 10),
    df["complexity"] > 10
]
choices = ["Low", "Medium", "High"]
df["complexity_level"] = np.select(
    conditions,
    choices,
    default="Unknown"
)


conditions = [
    (df["complexity"] > 10) & (df["changes"] > 20),

    (df["complexity"] > 10) | (df["changes"] > 20)
]
choices = ["High", "Medium"]
df["risk_level"] = np.select(
    conditions,
    choices,
    default="Low"
)

#create with apply()
def check_complexity(value):
    if value <= 5:
        return "Low"
    elif value <= 10:
        return "Medium"
    else:
        return "High"
    
df["complexity_level"] = df["complexity"].apply(
    check_complexity
)

#create with apply() : create mulit columns
df = df.assign(
    total=df["changes"] + df["complexity"]
)
df = df.assign(
    total=df["changes"] + df["complexity"],
    change_ratio=df["changes"] / df["lines"],
    average=(df["changes"] + df["complexity"]) / 2
)

df["row_mean"] = df[
    ["changes", "complexity", "lines"]
].mean(axis=1)