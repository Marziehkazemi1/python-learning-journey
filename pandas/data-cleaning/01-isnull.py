import pandas as pd
import numpy as np

data = {
    "changes": [10, 15, np.nan, 8, 30],
    "complexity": [5, 8, 10, np.nan, 15],
    "lines": [100, 150, 200, 80, 300],
    "defect": [0, 1, 1, 0, np.nan]
}

df = pd.DataFrame(data)

#isnull(): check value for each cell : True => is vacant   False => isnt vacant
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())   #count of all missing value
print(df.isnull().values.any())  #there is missing value or not?
print(df[df.isnull().any(axis=1)])   #show rows that have one missing value

#notnull(): On the contrary isnull(): True => isnt vacant  False => is vacant
print(df.notnull())
print(df.notnull().sum())
