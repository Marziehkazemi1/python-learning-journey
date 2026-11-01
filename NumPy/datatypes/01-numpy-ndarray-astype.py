import numpy as np

arr = np.array([10.5, 20.8, 30.2])

print(arr)
print(arr.dtype)

new_arr = arr.astype(int)
print("new_arr", new_arr)

#change to float
arr2 = np.array([1,2,3])
floar_arr = arr.astype(np.float64)
print("floar arr:", floar_arr)
print("floar arr type:", floar_arr.dtype)

#change number to str
arr3 = np.array([100,200,300])
str_arr = arr3.astype(str)
print("str arr:", str_arr)
print("str arr type:", str_arr.dtype)


#Example
arr4 = np.array([
    [2.9, 4.1, 6.8],
    [1.5, 3.7, 8.2]
])

new_arr4 = arr4.astype(np.int32)
result = new_arr4 * 2
print("new arr4:", new_arr4)
print("result:", result)
print("arr4 type:", arr4.dtype)
print("new arr4 type:", new_arr4.dtype)