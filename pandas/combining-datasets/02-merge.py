import pandas as pd
#That is, it connects two dataframes based on a common key.

df1 = pd.DataFrame({
    "module_id": [1, 2, 3, 4],
    "changes": [10, 15, 20, 8],
    "defect": [0, 1, 0, 1]
})

df2 = pd.DataFrame({
    "module_id": [1, 2, 3, 4],
    "complexity": [5, 8, 10, 3],
    "lines": [100, 150, 200, 80]
})
result = pd.merge(
    df1,
    df2,
    on="module_id"
)
print(result)


###########
df1 = pd.DataFrame({
    "module_id": [1, 2, 3, 4],
    "changes": [10, 15, 20, 8]
})

df2 = pd.DataFrame({
    "module_id": [2, 3, 4, 5],
    "complexity": [8, 10, 3, 12]
})

result = pd.merge(
    df1,
    df2,
    on="module_id",
    how="inner"     #Keeps only rows whose key exists in both dataframes
)
print(result)


result = pd.merge(
    df1,
    df2,
    on="module_id",
    how="left"    #Keeps all rows in df1, even if they have no equivalent in df2.
)
print(result)

result = pd.merge(
    df1,
    df2,
    on="module_id",
    how="right"    #Keeps all rows in df2, even if they have no equivalent in df2.
)
print(result)

result = pd.merge(
    df1,
    df2,
    on="module_id",
    how="outer"    #It holds all the keys in both dataframes.
)
print(result)


#The join key in two dataframes does not have the same name.
df1 = pd.DataFrame({
    "module_id": [1, 2, 3],
    "changes": [10, 15, 20]
})
df2 = pd.DataFrame({
    "id": [1, 2, 3],
    "complexity": [5, 8, 10]
})
result = pd.merge(
    df1,
    df2,
    left_on="module_id",
    right_on="id",
    how="inner"
)
print(result)


#indicator() : With it you can find out which dataframe each row comes from.
# result = pd.merge(
#     df1,
#     df2,
#     on="module_id",
#     how="outer",
#     indicator=True
# )
# print(result)


df1 = pd.DataFrame({
    "project": ["A", "A", "B", "B"],
    "module_id": [1, 2, 1, 2],
    "changes": [10, 15, 20, 25]
})

df2 = pd.DataFrame({
    "project": ["A", "A", "B", "B"],
    "module_id": [1, 2, 1, 2],
    "complexity": [5, 8, 10, 12]
})
result = pd.merge(
    df1,
    df2,
    on=["project", "module_id"],
    how="inner"
)
print(result)


#merge with index
df1 = pd.DataFrame({
    "changes": [10, 15, 20]
}, index=[1, 2, 3])
df2 = pd.DataFrame({
    "complexity": [5, 8, 10]
}, index=[1, 2, 3])

result = pd.merge(
    df1,
    df2,
    left_index=True,
    right_index=True
)
print(result)