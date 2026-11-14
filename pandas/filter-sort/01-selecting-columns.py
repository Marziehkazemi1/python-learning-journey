import pandas as pd

data = {
    "changes": [10, 15, 20, 8, 30],
    "complexity": [5, 8, 10, 3, 15],
    "lines": [100, 150, 200, 80, 300],
    "defects": [0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)
print(df)

#single column selection
print(df["changes"])
print(df.complexity)

#mulitple columns selection
print(df[["changes", "complexity"]])
print(df.loc[:, ["changes", "complexity"]]) 
print(df.loc[0:2, ["changes", "complexity"]])

print(df.iloc[:, 0:2])
print(df.iloc[:, [0, 3]])   #select column 1 and column 4

#select for filter()
print(df.filter(items=["changes", "lines"]))
print(df.filter(like="change"))  #Selecting columns whose names have a specific pattern

#drop() for delete columns
new_df = df.drop(columns=["lines", "changes"])
print(new_df)