import numpy as np
#for Calculations median in array

#first sort datas then number in middle is median
arr = np.array([10, 2, 8, 4, 6])
result = np.median(arr)
print("result:", result)

#for odd number  ==> tow numbers in middle with together plus then division 2
arr1 = np.array([2,4,5,7])
result1 = np.median(arr1)
print("result1:", result1)


#when axis=None ==> first change array to One-dimensional then calculations median
arr3 = np.array([
    [10,20,30],
    [40,50,60]
])
print("arr3:", np.median(arr3))

# if axis=0   ===> for each column calculations median Separately
print(np.median(arr3, axis=0))

# if axis=1  ==> for each row calculations median Separately
print(np.median(arr3, axis=1))