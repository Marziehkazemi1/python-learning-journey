class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def get_name(self):
        print("Name is %s" % self.name)

    def get_age(self):
        print("Age is %s" % self.age)

    def get_info(self):
        print("Name is %s and age is %i" % (self.name, self.age))

    def birthday(self):
        self.age += 1
        print("Happy birthday %s" % self.name)

    def return_count(self):
        return Person.count

marzieh = Person("marzi", 26)

marzieh.get_name()
marzieh.get_age()
marzieh.get_info()
marzieh.birthday()
marzieh.get_age()

print(marzieh.return_count())