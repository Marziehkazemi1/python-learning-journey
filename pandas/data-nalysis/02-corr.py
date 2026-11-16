import pandas as pd
#We use it to examine the relationship and degree of correlation between numerical variables.

data = {
    "changes": [10, 15, 20, 8, 30, 12, 25, 18],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180],
    "defect": [0, 1, 0, 1, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

corr_matrix = df.corr()
print(corr_matrix)

print(df["changes"].corr(df["complexity"]))

corr_matrix = df.corr()
print(corr_matrix["defect"])

print(df.corr(method="pearson"))

print(df.corr(method="spearman"))

print(df.corr()["defect"])

print(df.corr()["defect"].sort_values(
    ascending=False
))

print(df.corr()["defect"].drop("defect"))   #delete defect column from result

print(df.select_dtypes(
    include="number"
).corr())
