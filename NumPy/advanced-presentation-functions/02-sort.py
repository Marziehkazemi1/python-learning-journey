import numpy as np
#for sort of arrays
#return new array and not change original array

a = np.array([40, 10, 30, 20, 50])
result = np.sort(a)
print("Original:", a)
print("Sorted:", result)


b = np.array([
    [4, 1, 3],
    [9, 2, 6],
    [7, 5, 8]
])
print("b axis none",np.sort(a, axis=None))
print("b axis0",np.sort(b, axis=0))
print("b axis1",np.sort(b, axis=1))


c = np.array([10, 40, 20, 50, 30])
print("c:",np.sort(c, descending=True))     #descending parameter — Descending sort


d = np.array([40, 10, 30, 20])
#kind parameter — Sorting algorithm

print(np.sort(d, kind="quicksort"))
print(np.sort(d, kind="heapsort"))
print(np.sort(d, kind="stable"))


e = np.array([30, 10, 20, 10])
#stable parameter — stable sorting
print("e:",np.sort(e, stable=True))


people = np.array(
    [
        ("Sara", 25, 165.0),
        ("Ali", 20, 180.0),
        ("Reza", 25, 175.0)
    ],
    dtype=[
        ("name", "U10"),
        ("age", int),
        ("height", float)
    ]
)

print("sort age:",np.sort(people, order="age"))
print("sort age and hight:",np.sort(people, order=["age", "height"]))


f = np.array([5, -3, 10, -1, 0])
print("f:", np.sort(f))

g = np.array([4, 2, 4, 1, 2])
print("g:", np.sort(g))



#diffrent between sort() and argsort()  ===>  sort() The sorted values ​​themselves , argsort() indexes of sorted items
h = np.array([40, 10, 30, 20])
print("h:", np.sort(h))
print(np.argsort(h))