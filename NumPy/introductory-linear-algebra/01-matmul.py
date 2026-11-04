import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a * b)
print(np.matmul(a, b))    #or ===> a @ b
print(a @ b)    


c = np.array([1, 2, 3])
d = np.array([4, 5, 6])
print("resulr:", np.matmul(c, d))




inputs = np.array([[2, 3]])

weights = np.array([
    [0.5, 0.2],
    [0.3, 0.4]
])

output = np.matmul(inputs, weights)

print("output:", output)