import numpy as np
#var()  ===> Variance :  The standard deviation is the square root of the variance.

arr = np.array([[1,2],[3,4]])
print("", np.var(arr))
print("arr axis0",np.var(arr, axis=0))
print("arr axis1",np.var(arr, axis=1))


arr1 = np.zeros((2, 512*512), dtype=np.float32)   #array have 2 row and each row have 512*512 value
arr1[0, :] = 1.0   #all values in first row 1.0
arr1[1, :] = 0.1   #all values in second row 0.1
print("arr1",np.var(arr1))
print("arr1 float64",np.var(arr1, dtype=np.float64))   #float64 have accuracy higher than float32


arr2 = np.array([
    [14, 8, 11, 10],
    [7, 9, 10, 11],
    [10, 15, 5, 10]
])
print("arr2",np.var(arr2))
#where specifies which elements participate in the calculation
print("arr2 where",np.var(arr2, where=[[True], [True], [False]]))   #Consider the first two lines and discard the third line.