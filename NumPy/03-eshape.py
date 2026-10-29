import numpy as np;

a = np.arange(12)
print("a:", a)

# We want to convert this one-dimensional array into a 3x4 array.

b = a.reshape(3, 4)
print("b:", b)

#Now we have a multidimensional array, we want to make it one-dimensional.
c = b.reshape(-1)
print("c:", c)
#OR
d = b.ravel()
print("d:", d)

e = b.flatten()
print("e:", e)