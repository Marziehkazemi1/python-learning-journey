import numpy as np
#stack() creates a new axis, but concatenate() concatenates an existing axis.


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.stack((a, b))
result1 = np.concatenate((a, b))

print("result:", result)
print("result1:", result1)
print("result shape:", result.shape)

print("result axis0:", np.stack((a, b), axis=0))
print("result axis1:", np.stack((a, b), axis=1))
print("resulr axis-1:", np.stack((a, b), axis=-1))


#for 2D
arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

result2 = np.stack((arr1, arr2), axis=0)
result3 = np.stack((arr1, arr2), axis=1)

print("result2 axis0:", result2)
print("result3 axis1:", result3)
print("result2 shape", result2.shape)



#vstack() : To combine arrays along the vertical axis
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

result4 = np.vstack((x, y))
print("result4:", result4)
print(result4.shape)


p = np.array([
    [1, 2],
    [3, 4]
])

z = np.array([
    [5, 6],
    [7, 8]
])

result5 = np.vstack((p, z))

print("result5:", result5)
print(result5.shape)


#diffrent between:
w = np.array([1, 2, 3])
q = np.array([4, 5, 6])

print("vstack:", np.vstack((w, q)))
print("concatenate: ",np.concatenate((w, q)))
print("stack:", np.stack((w, q)))


#hstack() : Placing arrays horizontally or side by side.

#In one-dimensional arrays, hstack() stacks the array elements one after the other.
k = np.array([1, 2, 3])
c = np.array([4, 5, 6])
result6 = np.hstack((k, c))

print("result6:", result6)
print(result6.shape)



r = np.array([
    [1, 2],
    [3, 4]
])

n = np.array([
    [5, 6],
    [7, 8]
])

result7 = np.hstack((r, n))

print("result7:", result7)
print(result7.shape)