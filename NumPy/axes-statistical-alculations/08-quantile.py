import numpy as np
#Similar to percentile, except that the method of specifying percentile or quantile

arr = np.array([10, 20, 30, 40, 50])

print(np.quantile(arr, 0.25))
print(np.percentile(arr, 25))


arr1 = np.array([
    [10, 7, 4],
    [3, 2, 1]
])
np.quantile(arr1, 0.5, axis=0)
np.quantile(arr1, 0.5, axis=1)


arr2 = np.array([10, 20, 30, 40])

print(np.quantile(arr2, 0.25, method="linear"))   #linear: Interpolates between two close values; here the result is 17.5.
print(np.quantile(arr2, 0.25, method="lower"))    #lower: selects a lower value; 10
print(np.quantile(arr2, 0.25, method="higher"))   #higher: selects a higher value; 20