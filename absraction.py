from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Child Class
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child Class
class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Creating Objects
d = Dog()
c = Cat()

# Calling Methods
d.sound()
c.sound()