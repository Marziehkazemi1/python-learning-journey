import numpy as np;

A = np.arange(12).reshape(3,4)

print(A[A < 5])

three_up = (A >= 3)
print(A[three_up])

print(A[A % 2 == 1])

print(A[(A > 2) & (A < 11)])
print(A[(A < 2) | (A % 3 == 0)])