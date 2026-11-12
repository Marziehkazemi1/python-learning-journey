import pandas as pd
#value_counts() : for duplicate values
#nunique: for unique values

data = {
    "changes": [10, 15, 20, 8, 30, 12, 25, 18, 9, 22],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9, 4, 11],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180, 90, 220],
    "defect": [0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

print(df["defect"].value_counts())  #for count each item
print(df["defect"].value_counts(normalize=True)*100)
print(df["defect"].value_counts(ascending=True))  #sort datas 

print(df["defect"].nunique())
print(df["changes"].nunique())
print(df.nunique())
print(df.nunique(axis=1))