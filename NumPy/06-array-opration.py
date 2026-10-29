import numpy as np;

A = np.array([1,3,2,7])
B = np.array([4,1,1,3])


# for vector
print(np.add(A , B))

print(np.multiply(A, B))

print(np.power(A, B))

#for merix
X = np.array([[1,2], [3,4]])
Y = np.array([[3,1], [4,7]])

#Matrix multiplication
print(np.matmul(X, Y))