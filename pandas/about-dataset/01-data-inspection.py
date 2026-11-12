import pandas as pd

data = {
    "id": [101, 102, 103, 104, 105, 106, 107],
    "name": ["Ali", "Sara", "Reza", "Mina", "Amir", "Neda", "Arman"],
    "age": [22, 24, 21, 25, 23, 26, 22],
    "score": [18, 19, 15, 20, 17, 16, 19]
}

#head(): for see first rows: 5 row

df = pd.DataFrame(data)

print("head:",df.head())
print(df.head(3))

#tail(): for see last rows: 5 row
print("tail:", df.tail())
print(df.tail(2))

#sample(): Select random rows
print("sample:", df.sample(n=3))
print("frace:", df.sample(frac=0.5))   #Specifies the ratio of rows instead of the number.
print("random:", df.sample(n=3, random_state=42))   #for duplicated in random select
print("replace:", df.sample(n=10, replace=True))   #A row can be selected multiple times.
print("axis1", df.sample(n=2, axis=1))



data1 = {
    "changes": [10, 15, 20, 8, 30, 12, 25, 18, 9, 22],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9, 4, 11],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180, 90, 220],
    "defect": [0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data1)
print("head:", df.head())
print("tail:", df.tail(3))
print("sample:", df.sample(n=4))
print("frac:", df.sample(frac=0.5))
print("random state", df.sample(n=3, random_state=42))
print("random:", df.sample(n=2, axis=1))