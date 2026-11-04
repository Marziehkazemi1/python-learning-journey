import numpy as np
#To solve a system of linear equations

#for example
# {x + 2y = 5
# {3x + 4y = 11

A = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([5, 11])

result = np.linalg.solve(A, b)

print(result)   #[1 2]  ==> x=1 , y=2


# {x + y = 7
# {2x + y = 11
C = np.array([
    [1, 1],
    [2, 1]
])
d = np.array([7, 11])
result1 = np.linalg.solve(C, d)
print("C:", result1)



# {2x + 3y = 12
# {x + y = 5

E = np.array([
    [2, 3],
    [1, 1]
])
f = np.array([12, 5])
print("resule2:", np.linalg.solve(E, f))