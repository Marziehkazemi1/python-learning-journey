import pandas as pd

data = {
    "module": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "project": ["P1", "P1", "P2", "P2", "P1", "P2", "P2","P1"],
    "changes": [10, 15, 20, 8, 30, 12, 25, 18],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180],
    "defect": [0, 1, 0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
print(df)

print(df.groupby("defect"))
print(df.groupby("defect").mean(numeric_only=True))
print(df.groupby("defect")["complexity"].mean())
print(df.groupby("defect")[["changes", "complexity"]].mean())
print(df.groupby("defect")["changes"].sum())
print(df.groupby("defect")["complexity"].count())    #count of not missing value
print(df.groupby("defect").size())

#agg() : For multiple simultaneous calculations
print(df.groupby("defect")["complexity"].agg(    
    ["mean", "min", "max"]
))
print(df.groupby("defect").agg({
    "changes": ["mean", "max"],
    "complexity": ["mean", "std"],
    "lines": ["min", "max"]
}))
#we can change name of columns
print(df.groupby("defect").agg(
    avg_changes=("changes", "mean"),
    avg_complexity=("complexity", "mean"),
    max_lines=("lines", "max"),
    module_count=("module", "count")
))

#as_index
df.groupby(
    "defect",
    as_index=False
)["complexity"].mean()


#Grouping by multiple columns
print(df.groupby(["project", "defect"])["complexity"].mean())

#get_group() : access and see to spical group
print(df.groupby("defect").get_group(1))
print(df.groupby("project").get_group("P1"))
