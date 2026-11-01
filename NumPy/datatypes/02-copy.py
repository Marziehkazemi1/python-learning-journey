import numpy as np
# for create indepentet copy from array
#when we want change things on array but we dont want change things on first array

#in this example first array change
arr = np.array([10,20,30])
new_arr = arr
new_arr[0] = 100
print("arr:", arr)
print("new arr:", new_arr)

#for use copy()
arr1 = np.array([50,70,90])
new_arr1 = arr1.copy()
new_arr1[0] = 800
print("arr1:", arr1)
print("new arr1:", new_arr1)


#for object
arr2 = np.array([[1, 2], [3, 4]], dtype=object)
new_arr2 = arr2.copy()
new_arr2[0][0] = 100
print("arr2:", arr2)

#exm
arr3 = np.array([5, 10, 15])

a = arr
b = arr.copy()

a[0] = 50
b[1] = 100

print("arr3:",arr3)
print(a)
print(b)


#diffrent with copy() and view()
#in view firest array change
arr4 = np.array([10, 20, 30])

v = arr4.view()

v[0] = 100

print("arr:", arr4)
print("v:", v)



#exm
arr5 = np.array([1, 2, 3])

a = arr5.view()
b = arr5.copy()

a[1] = 20
b[2] = 30

print("arr5:", arr5)
print(a)
print(b)