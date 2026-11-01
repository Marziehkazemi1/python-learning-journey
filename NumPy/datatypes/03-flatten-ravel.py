import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])
new_arr = arr.flatten()
print("new arr:", new_arr)

###########
#diffrent between flatten and ravel
#flatten() ===> create a copy and not change original array
#ravel() ===> change original array

arr1 = np.array([
    [1,2],
    [3,4]
])

a = arr1.flatten()
b = arr1.ravel()
a[0] = 100
b[1] = 200
print("arr1:", arr1)

