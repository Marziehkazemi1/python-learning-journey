import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))



c = np.array([[1, 2],
              [3, 4]])

d = np.array([[5, 6],
              [7, 8]])

print(np.dot(c, d))


e = np.ones((2, 3, 4))
f = np.ones((2, 4, 5))

print(np.dot(e, f).shape)
print(np.matmul(e, f).shape)