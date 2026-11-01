import numpy as np
#In a two-dimensional array, this usually means converting rows to columns and columns to rows.

arr = np.array([
    [1,2,3],
    [4,5,6]
])
result = np.transpose(arr)
print("result:", result)