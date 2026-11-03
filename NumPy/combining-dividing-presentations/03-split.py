import numpy as np
#To divide an array into multiple subarrays

a = np.array([10, 20, 30, 40, 50, 60])
result = np.split(a, 3)   #Divide into 3 equal parts.
result1 = np.split(a, [2, 4])

print("result:", result)
print("result1:", result1)



b = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print("b axis0:",np.split(b, 2, axis=0))
print("b axis1:",np.split(b, 2, axis=1))


#vsplit()
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

print("arr:",np.vsplit(arr, 2))
print(np.vsplit(arr, [1, 3]))

#hsplit()
arr1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print("arr1:", np.hsplit(arr1, 2))