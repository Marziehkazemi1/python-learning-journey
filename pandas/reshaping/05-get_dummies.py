import pandas as pd
#To convert categorical variables

df = pd.DataFrame({
    "module": ["Login", "Payment", "Dashboard", "Login", "Payment"],
    "language": ["Python", "Java", "Python", "Java", "Python"],
    "changes": [10, 20, 15, 8, 25],
    "defect": [1, 0, 1, 0, 1]
})

print(df)

encoded = pd.get_dummies(df["language"])
df = pd.concat([df, encoded], axis=1)
print(df)

df_encoded = pd.get_dummies(
    df,
    columns=["module", "language"],
    prefix="lang"    #Used to specify the prefix for new column names.
)
print(df_encoded)