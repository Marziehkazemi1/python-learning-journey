import numpy as np
#It is used to calculate the inverse of a matrix.
#What matrices have an inverse?
#Not every matrix is ​​invertible.

#For a matrix to have an inverse:
# It must be square; for example, 2x2 or 3x3.
# Its determinant must not be zero.

A = np.array([
    [1, 2],
    [3, 4]
])

A_inv = np.linalg.inv(A)

print(A_inv)


B = np.array([
    [2, 0],
    [0, 4]
])

B_inv = np.linalg.inv(B)
print(B_inv)


C = np.array([[[1., 2.], [3., 4.]], [[1, 3], [3, 5]]])
print("C:", np.linalg.inv(C))