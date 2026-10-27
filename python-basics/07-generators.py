def firstn():
    yield 1
    yield 2
    yield 3

for i in firstn():
    print(i)


def firstt(n):
    num = 0

    while num < n:
        yield num
        num += 1

for i in firstt(10):
    print(i)