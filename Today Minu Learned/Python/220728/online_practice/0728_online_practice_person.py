class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        cls.name = name
        cls.year = year

    def check_age(self):
        if self.age >= 19:
            return False
        else:
            return True

apple = Person.details('apple', 1982)
samsung = Person('samsung', 18)

print(apple)

print(Person.check_age(samsung))