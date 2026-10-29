import numpy as np;

A = np.arange(3, 9)

#How to access indexes
#if array vector

print("A[0]:", A[0])
print("A[1]:", A[1])
print("A[2:]:", A[2:])
print("A[-3:]:", A[-3:])
print("A[2:4]:", A[2:4])


#if merix
B = np.arange(12).reshape(3, 4)

print("B[0]:", B[0])
print("B[0,1]:", B[0,1])
print("B[0,1:]:", B[0, 1:])
print("B[0,:]:", B[0,:])
print("B[1, -2:]:", B[1, -2:])
print("B[2, 1:3]:", B[2, 1:3])