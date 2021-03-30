# static and Class methods
class Person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getpopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')

newperson = Person("tim", 18)
# using a print to demonstrate the ( @classmethod )
print(Person.getpopulation())
# using a print to demonstrate the ( @staticmethod )
print(Person.isAdult(21))
print(Person.isAdult(21))