import pandas as pd

data = {
    "changes": [10, 15, 20, 8, 30],
    "complexity": [5, 8, 10, 3, 15],
    "lines": [100, 150, 200, 80, 300],
    "defect": [0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

df = df.rename(
    columns={"changes": "num_changes"}
)

df = df.rename(
    columns={
        "changes": "num_changes",
        "complexity": "code_complexity",
        "lines": "loc"
    }
)

df.columns = [
    "num_changes",
    "code_complexity",
    "loc",
    "defect"
]


#inplace : return new dataframe
df.rename(
    columns={"changes": "num_changes"},
    inplace=True
)


#we can change index and than rename index 
df = pd.DataFrame(
    {
        "changes": [10, 15, 20],
        "complexity": [5, 8, 10]
    },
    index=["A", "B", "C"]
)

df = df.rename(
    index={
        "A": "Module_A",
        "B": "Module_B",
        "C": "Module_C"
    }
)