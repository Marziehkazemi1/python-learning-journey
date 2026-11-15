import pandas as pd
import numpy as np

data = {
    "changes": [10, 15, -1, 8, 30, -1, 25, 18],
    "complexity": [5, 8, 10, 3, 15, 6, 12, 9],
    "lines": [100, 150, 200, 80, 300, 120, 250, 180],
    "defect": [0, 1, 0, 1, 1, 0, 1, 0],
    "status": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No"]
}

df = pd.DataFrame(data)

#df.replace(old_value, new_value)
df["changes"] = df["changes"].replace(-1, 0)    #values -1 replace 0

df["status"] = df["status"].replace({
    "Yes": 1,
    "No": 0
})


df = df.replace({     #change all dataframe
    "Yes": 1,
    "No": 0
})

df = df.replace({
    "changes": {-1: np.nan},
    "status": {"Yes": 1, "No": 0}
})
