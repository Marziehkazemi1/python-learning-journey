import pandas as pd

data = {
    "changes": [10, 15, 20, 8, 30, 12, 25, 18, 9, 22],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9, 4, 11],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180, 90, 5000],
    "defect": [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

#1: Calculating quartiles
Q1 = df["lines"].quantile(0.25)
Q3 = df["lines"].quantile(0.75)

print("Q1:", Q1)
print("Q3:", Q3)

#2: calculate IQR
IQR = Q3 - Q1

#3: Calculating the allowable range
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

#4:Identifying outliers
outliers = df[
    (df["lines"] < lower_bound) |
    (df["lines"] > upper_bound)
]
print(outliers)

df["is_outlier"] = ~df["lines"].between(
    lower_bound,
    upper_bound
)


#use z-score for qutlier detection
mean = df["lines"].mean()
std = df["lines"].std()

df["z_score"] = (
    df["lines"] - mean
) / std
outliers = df[
    df["z_score"].abs() > 3
]
print(outliers)




numeric_df = df.select_dtypes(include="number")

for col in numeric_df.columns:

    Q1 = numeric_df[col].quantile(0.25)
    Q3 = numeric_df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = numeric_df[
        (numeric_df[col] < lower) |
        (numeric_df[col] > upper)
    ]

    print(col, len(outliers))
