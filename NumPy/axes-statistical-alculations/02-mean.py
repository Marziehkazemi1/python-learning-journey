import numpy as np
#calculation mean all of numbers ====> total numbers division on count of numbers
#diffrent median() and mean()  ==>  mean(): calculation mean all of numbers    median(): Finds the middle value of sorted data.

arr = np.array([10, 20, 30, 40, 100])
result_mean = np.mean(arr)
result_median = np.median(arr)
print("result mean:", result_mean)
print("result median:", result_median)


arr1 = np.array([
    [10,20,30],
    [40,50,60]
])
print("arr1 axis=0:", np.mean(arr1, axis=0))   #calculation mean for each cloumn
print("arr1 axis=1:", np.mean(arr1, axis=1))   #calculation mean for each row
