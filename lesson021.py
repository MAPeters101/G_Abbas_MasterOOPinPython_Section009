from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def whatIEat(self):
        pass

class Lion(Animal):
    def whatIEat(self):
        print("Lion eats meat")

class Cow(Animal):
    def whatIEat(self):
        print("Cow eats grass")

class Dog(Animal):
    def whatIEat(self):
        print("Dog eats dog food.")


lion = Lion()
lion.whatIEat()

cow = Cow()
cow.whatIEat()

dog = Dog()



