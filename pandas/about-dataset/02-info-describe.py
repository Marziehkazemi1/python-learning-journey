import pandas as pd

#info(): talk about data structue
#describe(): talk about What is the statistical status of the numerical values ​​in the dataset

data = {
    "id": [101, 102, 103, 104, 105, 106, 107],
    "name": ["Ali", "Sara", "Reza", "Mina", "Amir", "Neda", "Arman"],
    "age": [22, 24, 21, 25, 23, 26, 22],
    "score": [18, 19, 15, 20, 17, 16, 19]
}

df = pd.DataFrame(data)

print("info:", df.info())
print("verbose:", df.info(verbose=True))
print("show count:", df.info(show_counts=True))

print("describe:", df.describe())
print(df.describe().loc["count"])
print(df.describe().loc["mean"])
print(df["changes"].mean())
print(df["changes"].std())
print(df["changes"].min())
print(df["changes"].max())
print(df["changes"].median())
print(df["changes"].quantile(0.25))
print(df["changes"].quantile(0.75))
#by include can specify datat type of cloumns 
print("incliude:",df.describe(include="all"))   #all: all of coumns
print(df.describe(include="number"))   #just numerical columns
print(df.describe(include="number"))   #just object columns
print("percentiles:", df.describe(
    percentiles=[0.1, 0.25, 0.5, 0.75, 0.9]
))
print(df.describe(exclude="number"))   #for delete one type of datas
