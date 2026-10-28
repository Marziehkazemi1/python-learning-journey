#One of the important concepts of numpy is ndarray, which is an array of objects of the same type. It is better than a normal list because it is faster and because all elements are of the same type, it occupies less data volume.
#In the real world, they model 3 things: vector, which is a one-dimensional array,
#metrix, which is a two-dimensional array, and tensor, which is more than two dimensions.

import numpy as np

#vector
A = np.array([1,2,3,4])
print(A[0], A[1])

X = np.ones(3) #A one-dimensional array has 3 elements, all of which are one.
Y = np.zeros(5) #A one-dimensional array has 5 elements, all of which are zero.
Z = np.empty(2)  #Randomly, depending on where in memory the variable z is filled.and cteated more sped.

print("X:", X)
print("Y:", Y)
print("Z:", Z)

T = np.arange(4)
print(T)

T1 = np.arange(2, 9, 2)
print(T1)

S = np.linspace(0 , 13, num = 5)  #Between two ranges that each contain two numbers, we can specify the numbers we want. It returns numbers in the range num = 5 such that the intervals between the numbers are the same.
print(S)


#merix
F = np.array([
    [0,1,2,3],
    [4,5,6,7],
    [8, 9, 10, 11] 
])

print("F", F.ndim)
print("F", F.size)  #count of array
print("F", F.shape)  #It says how many elements we have on each axis.

#tensor
D = np.array([
    [
        [0,1,2,3],
        [4,5,6,7],
        [8, 9, 10, 11] 
    ],
    [
        [0,1,2,3],
        [4,5,6,7],
        [8, 9, 10, 11] 
    ]
])

print("D", D.ndim)
print("D", D.size)
print("D", D.shape)