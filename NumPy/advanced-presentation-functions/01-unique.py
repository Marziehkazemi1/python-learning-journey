import numpy as np
#fro finding unique and non-duplicate values ​​in an array

a = np.array([30, 10, 30, 20, 10])
result = np.unique(a)
print("result:", result)
print("return_index=True:", np.unique(a, return_index=True))   #Index of the first occurrence
print("return_counts=True:", np.unique(a, return_counts=True))  #Number of repetitions of each value
print("return_inverse=True:", np.unique(a, return_inverse=True))     #Rebuilding the original array

b = np.array([
    [1, 2],
    [1, 2],
    [3, 4],
    [1, 2]
])
print("b:", np.unique(b))
print("b axis0:", np.unique(b, axis=0))   #Duplicate rows are removed.
print("b axis1:", np.unique(b, axis=1))   #Duplicate columns are removed.


c = np.array([50, 10, 10, 80, 60, 40, 60])
values, indices, inverse, counts = np.unique(
    c,
    return_index=True,
    return_inverse=True,
    return_counts=True
)
print("Values:", values)
print("Indices:", indices)
print("Inverse:", inverse)
print("Counts:", counts)