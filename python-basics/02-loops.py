n = 3

while n > 0:
    print(n)
    n += 1

    if n == 100:
        break

friends = ["marzi", "razi", "zahra"]
count = 0

for person in friends:
    print("Hi", person)
    count += 1

print("I said", count, "hi")