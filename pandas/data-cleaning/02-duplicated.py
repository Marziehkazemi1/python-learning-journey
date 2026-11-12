import pandas as pd

data = {
    "changes": [10, 15, 20, 10, 30, 15],
    "complexity": [5, 8, 10, 5, 15, 8],
    "lines": [100, 150, 200, 100, 300, 150],
    "defect": [0, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

#duplicated(): which rows duplicated: True => this row is duplicated  False => this row not duplicated
print(df.duplicated())
print("sum:",df.duplicated().sum())   #count of rows duplicates
print(df[df.duplicated()])   #show duplicates row
print(df.duplicated(subset=["changes", "complexity"]))  #show duplicat base of name column


#drop_duplicates(): remove duplicated rows
print(df.drop_duplicates())
print(df.drop_duplicates(subset=["changes"]))
print(df.drop_duplicates(inplace=True))  #change orifinal dataframe