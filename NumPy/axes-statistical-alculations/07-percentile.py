import numpy as np
#Used to calculate percentiles 
#The percentile tells us what value falls in a specific position in the sorted data.

arr = np.array([10,20,30,40,50,60,70])
#Here we say, for example, what percentile do we want?
print(np.percentile(arr, 25))
print(np.percentile(arr, 50))
print(np.percentile(arr, 75))
print(np.percentile(arr, 100))
print(np.percentile(arr, [25, 50, 75]))


arr1 = np.array([
    [10, 7, 4],
    [3, 2, 1]
])
print("arr1:", np.percentile(arr1, 50))
print("arr1 axis0:", np.percentile(arr1, 25, axis=0))
print("arr1 axis1:", np.percentile(arr1, 25, axis=1))



#The parameter overwrite_input=True. This means we allow NumPy to modify the input array to use the available memory for calculating the percentile.
a = np.array([[10, 7, 4], [3, 2, 1]]) 
b = a.copy()
np.percentile(b, 50, axis=1, overwrite_input=True)
assert not np.all(a == b)
print("a:", a)
print("b:", b)
print("Equal:", np.all(a == b))