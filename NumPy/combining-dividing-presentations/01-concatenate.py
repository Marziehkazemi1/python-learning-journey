import numpy as np
#for paste many arrays to one array

arr1 = np.array([1,2,3,4])
arr2 = np.array([4,5,6,7])

result = np.concatenate((arr1, arr2))
print("result:", result)


a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])
result1 = np.concatenate((a, b), axis=0)   #concatenate array column
result1 = np.concatenate((a, b), axis=1)   #concatenate array row
print("result1 axis0:",result1)
print("result1 axis1:",result1)


#To concatenate two 2D arrays with axis=0, their number of columns must be equal.
a1 = np.array([[1, 2], [3, 4]])  # shape = (2, 2)
b1 = np.array([[5, 6]])          # shape = (1, 2)

print(np.concatenate((a1, b1), axis=0))