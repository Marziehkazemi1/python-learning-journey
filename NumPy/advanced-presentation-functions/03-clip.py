import numpy as np
#Used to limit the values ​​of an array to a specific range.

a = np.array([5, 15, 25, 50, 85, 100, 120])
result = np.clip(a, 20, 80)
print("result:", result)
#The number 5 is less than the minimum of 20; so it becomes 20.
#The number 15 also becomes 20.
#The numbers 25 and 50 are in the range; so they do not change.
#The numbers 85, 100, and 120 are greater than the maximum of 80; so they become 80.


b = np.array([-20, -10, 0, 10, 20, 30])
print("b:", np.clip(b, 0, None))


c = np.array([10, 20, 40, 60, 80, 100])
#No number is greater than 50.
print("c:", np.clip(a, None, 50))


d = np.array([
    [-10, 20, 150],
    [30, 80, 200],
    [5, 60, 100]
])
print("d:", np.clip(d, 0, 100))


e = np.array([10, 50, 100, 150])
minimum = np.array([20, 40, 80, 120])
maximum = np.array([30, 60, 90, 140])
print("e:", np.clip(e, minimum, maximum))


f = np.array([5, 20, 50, 100])
out = np.empty_like(f)
print("f:", np.clip(f, 10, 80, out=out))