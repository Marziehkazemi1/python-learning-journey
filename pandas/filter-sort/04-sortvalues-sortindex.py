import pandas as pd

data = {
    "name": ["Ali", "Sara", "Reza", "Mina", "John"],
    "age": [25, 20, 30, 22, 28],
    "score": [85, 95, 70, 90, 80],
    "salary": [3000, 4500, 2500, 4000, 3500]
}

df = pd.DataFrame(data)
print(df)

#sort_values() : to sort by column values ​​or values ​​in a Series
print(df.sort_values(by="age"))    #sort by age
print(df.sort_values(by="age", ascending=False))   #sort descending
print(df.sort_values(by=["age", "score"]))
print(
    df.sort_values(
        by=["age", "score"],
        ascending=[True, False]
    )
)

#sort_index() : to sort by Index or row and column labels
data1 = {
    "name": ["Ali", "Sara", "Reza", "Mina"],
    "score": [85, 95, 70, 90]
}
df1 = pd.DataFrame(
    data1,
    index=[3, 1, 4, 2]
)
print(df1)

print(df1.sort_index())   #sort index Ascending
print(df1.sort_index(ascending=False))  #sort index descending


