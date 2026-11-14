import pandas as pd
import numpy as np

data = {
    "name": ["Ali", "Sara", "Reza", "Mina", "John"],
    "age": [25, np.nan, 30, 22, np.nan],
    "score": [85, 95, np.nan, 90, 80],
    "city": ["Tehran", "London", None, "Berlin", "Paris"]
}

df = pd.DataFrame(data)

print(df)


#dropna() : for delete missing datas
print(df.dropna())  #delete rows missing value
print(df.dropna(axis=1))   #delete columns missing value
print(df.dropna(how="any"))   #If there is at least one Missing value, the row is deleted. 
print(df.dropna(how="all"))   #if there is all value missing value, the row is deleted
print(
    df.dropna(
        subset=["age", "score"]
    )
)  #just check age and score columns
print(df.dropna(thresh=2))    #Each row or column must have at least a few non-Missing values ​​to be preserved.


#fillna() : Replaces missing values ​​with other values.
print(df.fillna(0))
df["age"] = df["age"].fillna(0)
df = df.fillna({
    "age": 0,
    "score": 50
})

mean_age = df["age"].mean()
df["age"] = df["age"].fillna(mean_age)

median_age = df["age"].median()
df["age"] = df["age"].fillna(median_age)

mode_age = df["age"].mode()[0]    #Mode is the most frequent value.
df["age"] = df["age"].fillna(mode_age)