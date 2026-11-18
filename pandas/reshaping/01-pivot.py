import pandas as pd
#use for reshaping dataframe
#Take the values ​​of one column and convert them into new column names.

df = pd.DataFrame({
    "module": ["A", "A", "B", "B", "C", "C"],
    "metric": ["changes", "complexity", "changes", "complexity", "changes", "complexity"],
    "value": [10, 5, 15, 8, 20, 10]
})
print(df)

#index specifies which columns will form the output rows
#columns specifies which column values ​​will be converted into new columns
#values ​​specifies which column values ​​will be placed into cells

result = df.pivot(
    index="module",
    columns="metric",
    values="value"
)

print(result)

#The combination of index and columns in pivot() must be unique. we use pivot_table()
#Capable of performing statistical calculations on repeated values
df1 = pd.DataFrame({
    "project": ["A", "A", "A", "B", "B"],
    "module": ["M1", "M1", "M2", "M1", "M2"],
    "metric": ["changes", "complexity", "changes", "changes", "complexity"],
    "value": [10, 5, 15, 20, 8]
})

result = df1.pivot_table(
    index="module",
    columns="metric",
    values="value",
    aggfunc="mean"  #How many values ​​were there for a house, how to aggregate them
)
print(result)

result = df1.pivot_table(
    index=["module", "version"],
    columns="metric",
    values="value",
    aggfunc="mean",
    fill_value=0  #We don't want to have NaN values ​​in the output.
)

result = df1.pivot_table(
    index="project",
    columns=["metric","module"],
    values="value",
    aggfunc="mean",
    margins=True,     #An additional row and column named All will be created, showing the overall statistics.
    margins_name="Total"
)
print(result)
