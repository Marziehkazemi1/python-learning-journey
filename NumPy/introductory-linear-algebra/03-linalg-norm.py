import numpy as np
#Used to calculate the size or length of a vector or matrix.

a = np.array([3, 4])
print(np.linalg.norm(a))


b = np.array([3, -4])

print(np.linalg.norm(b))       # 5.0    The square root of the sum of the numbers
print(np.linalg.norm(b, ord=1)) # 7.0   Absolute sum of numbers   |3| + |-4| = 7
print(np.linalg.norm(b, ord=np.inf)) # 4.0   The greatest absolute value of a number   max(|3|, |-4|) = 4


c = np.array([
    [3, 4],
    [5, 12]
])

print(np.linalg.norm(c, axis=1))
print(np.linalg.norm(c, axis=0))
