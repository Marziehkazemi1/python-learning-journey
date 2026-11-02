import numpy as np
#argmax() : Returns the index of the largest value in the array, not the largest value itself.

arr = np.array([10, 50, 30, 90, 20])

print("arr max:", np.max(arr))
print("arr argmax:", np.argmax(arr))


arr1 = np.arange(6).reshape(2, 3) + 10
print("arr1:", arr1)
print("arr1 argmax:", np.argmax(arr1))


arr2 = np.array([
    [10,50,90],
    [40,80,60]
])
print("arr2 axis0", np.argmax(arr2, axis=0))    #The largest index each column
print("arr2 axis1", np.argmax(arr2, axis=1))    #The largest index each row



#argmin() : Returns the index of The smallest value in the array, not the largest value itself.
arr3 = np.array([10,50,70,40,5,30])
print("arr3:", np.argmin(arr3))

arr4 = np.array([
    [10, 5, 8],
    [3, 7, 2]
])
print("arr4 axis0", np.argmin(arr4, axis=0))
print("arr4 axis1", np.argmin(arr4, axis=1))


