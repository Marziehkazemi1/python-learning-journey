import pandas as pd
#The melt() method does the exact opposite of what pivot() does.
#If in pivot() we converted the data from rows to columns, in melt() we convert the columns to rows.

df = pd.DataFrame({
    "module": ["A", "B", "C"],
    "changes": [10, 15, 20],
    "complexity": [5, 8, 10],
    "lines": [100, 150, 200]
})

print(df)

#id_vars : Specifies which columns should remain fixed and not be moved to new rows.
#value_vars : Specifies which columns should be converted to rows.
#var_name : Specifies a new column name that retains the names of the previous columns.
#value_name : Specifies the name of the column where the numeric values ​​will be placed.

result = df.melt(
    id_vars=["module"],
    value_vars=["changes", "complexity", "lines"],
    var_name="metric",
    value_name="value"
)

print(result)

df1 = pd.DataFrame({
    "module": ["A", "B", "C"],
    "project": ["P1", "P1", "P2"],
    "defect": [0, 1, 0],
    "changes": [10, 15, 20],
    "complexity": [5, 8, 10],
    "lines": [100, 150, 200]
})

result = df1.melt(
    id_vars=["module", "project", "defect"],
    value_vars=["changes", "complexity", "lines"],
    var_name="metric",
    value_name="value",
    ignore_index=False
)

print(result)
