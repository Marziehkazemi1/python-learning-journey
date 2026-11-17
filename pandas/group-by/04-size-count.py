import pandas as pd
import numpy as np

data = {
    "module": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "changes": [10, 15, 20, 8, 30, 12, 25, 18],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180],
    "defect": [0, 1, 0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

#size() : counts the total number of rows in each group.
#count() : counts the number of non-missing (Non-Null) values ​​in each column.

print(df.groupby("defect").size())

print(df.groupby("defect").count())

df.loc[0, "changes"] = np.nan
print(df.groupby("defect").size())
print(df.groupby("defect").count())    #one of the item in changes column is nan

print(df.groupby("defect")["changes"].count())
print(df.groupby("defect")["module"].count())



