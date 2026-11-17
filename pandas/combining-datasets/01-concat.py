import pandas as pd

df1 = pd.DataFrame({
    "module": ["A", "B", "C"],
    "changes": [10, 15, 20],
    "defect": [0, 1, 0]
})

df2 = pd.DataFrame({
    "module": ["D", "E", "F"],
    "changes": [8, 30, 12],
    "defect": [1, 1, 0]
})

result = pd.concat(
    [df1, df2],
    axis=0   #contact columns
)
print(result)

result = pd.concat(
    [df1, df2],
    axis=0,   #contact columns
    ignore_index=True   #Indexes are rebuilt from scratch.
)
print(result)

result = pd.concat(
    [df1, df2],
    axis=1   #contact rows
)
print(result)


df1 = pd.DataFrame({
    "module": ["A", "B"],
    "changes": [10, 15]
})

df2 = pd.DataFrame({
    "module": ["C", "D"],
    "changes": [20, 25]
})

result = pd.concat(
    [df1, df2],
    keys=["dataset_1", "dataset_2"]
)

print(result)

#verify_integrity : Sometimes you don't want to have duplicate indexes on the join axis.