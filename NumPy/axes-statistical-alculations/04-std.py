import numpy as np

#std() for Standard deviation and data dispersion

arr = np.array([10,20,30,40,50])
result = np.std(arr)
print("result:", result)


arr1 = np.array([
    [10,20,30],
    [40,50,60]
])
print("arr1 axis0" , np.std(arr1, axis=0))     #std for each column
print("arr1 axis1" , np.std(arr1, axis=1))     #std for each row



arr3 = np.array([10,20,30,40,50])
print("arr3 ddof0", np.std(arr3, ddof=0))    #ddof=0  default and 
print("arr3 ddof1", np.std(arr3, ddof=1))    #If the data is a sample from a larger population, it is usually used to calculate the sample standard deviation from ddof=1.
