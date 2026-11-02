import numpy as np

arr = np.array([10,20,30,40,50])
result = np.sum(arr)
print("result:" ,result)


arr1 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(np.sum(arr1, axis=0))
print(np.sum(arr1, axis=1))

#with initial  ==> Start the sum with the initial value.
arr3 = np.array([1, 2, 3])
print(np.sum(arr3, initial=10))