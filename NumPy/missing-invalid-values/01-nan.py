import numpy as np

print(np.isnan(np.nan))
print(np.isnan(24))


a = np.array([10, np.nan, 30, np.nan, 50])
result = np.isnan(a)
print(result)
print(np.sum(result))


#for 2D
b = np.array([
    [10, np.nan, 30],
    [np.nan, 50, 60]
])

print("b:", np.isnan(b))