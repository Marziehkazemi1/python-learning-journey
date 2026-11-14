import pandas as pd
import numpy as np
#isna(), notna()  useing for missing data

data = {
    "name": ["Ali", "Sara", "Reza", "Mina", "John"],
    "age": [25, np.nan, 30, 22, np.nan],
    "score": [85, 95, np.nan, 90, 80]
}
df = pd.DataFrame(data)
print(df)


#isna() : check each cell have missing value or not have: for missing value return True
print(df.isna())
print(df["age"].isna())
print(df[df["age"].isna()])   #for find rows NaN
print(df[df[["age", "score"]].isna().any(axis=1)])
print(df[df[["age", "score"]].isna().all(axis=1)])
print(df.isna().sum())
print(df.isna().sum().sum())
print(df.isna().mean() * 100)


#notna() : Checks whether the value exists or not : if not exists return True
print(df.notna())
print(df[df["age"].notna()])
print(
    df[
        df["age"].notna() &
        df["score"].notna()
    ]
)
