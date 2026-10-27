import random

result = random.randint(1, 99)
name = input("What is your name? ")
guess = int(input("Guess the number: "))

while guess != result:
    if guess > result:
        print("My number is smaller!")
    else:
        print("My number is larger!")

    guess = int(input("Guess the number: "))

print("Wow!", name, "you did it!")