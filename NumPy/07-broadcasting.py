import numpy as np;

A = np.array([1,2,3])
B = 2
print(A * 2)

A = np.array([[1,2,3], [4,5,6]])
B = np.array([1,2,3])
C = A + B
print("C:", C)

A = np.array([[0], [10], [20], [30]])
B = np.array([0,1,2])
print(A + B)

F = np.array([1,2,3,4,5])
mean = F.mean()
std = F.std()
normalized_F = (F - mean) / std
print(normalized_F)