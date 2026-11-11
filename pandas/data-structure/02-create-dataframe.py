import pandas as pd
import numpy as np
#for create dataframe in pandas, we have 3 way:
#create dataframe from Dictionary
#create dataframe from List and List of Dictionaries
#create dataframe from Numpy

#create dataframe from Dictionary:
data = {
    "name": ["Ali", "Sara", "Reza"],
    "age": [22, 24, 23],
    "score": [18, 20, 15]
}

df = pd.DataFrame(data)
print("df:", df)

df = pd.DataFrame.from_dict(data)    #for create dataframe from dictionary
print(df)

#create dataframe from List
#1. simple list
data = [10, 20, 30, 40]
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, columns=["score"])
print(df)

#list of list
data = [
    ["Ali", 22, 18],
    ["Sara", 24, 20],
    ["Reza", 23, 15]
]

df = pd.DataFrame(
    data,
    columns=["name", "age", "score"]
)
print(df)

#List of Dictionaries
data = [
    {"name": "Ali", "age": 22},
    {"name": "Sara", "age": 24},
    {"name": "Reza", "age": 23}
]
df = pd.DataFrame(data)
print(df)

data = [
    {"name": "Ali", "age": 22},
    {"name": "Sara", "score": 20},
    {"name": "Reza", "age": 23, "score": 15}
]
df = pd.DataFrame(data)
print(df)

#create dataframe from Numpy
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(
    data,
    columns=["A", "B", "C"]
)
print(df)

df = pd.DataFrame(
    data,
    index=["first", "second", "third"],
    columns=["A", "B", "C"]
)
print(df)
print(df.loc["second", "B"])

data = np.array([10, 20, 30, 40]).reshape(1, 4)
df = pd.DataFrame(
    data,
    columns=["A", "B", "C", "D"]
)
print(df)

changes = np.array([10, 20, 30])
complexity = np.array([5, 8, 12])
defect = np.array([0, 1, 0])
df = pd.DataFrame({
    "changes": changes,
    "complexity": complexity,
    "defect": defect
})
print(df)