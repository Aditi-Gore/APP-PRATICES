# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")

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

# Calling the Same Method
d.sound()
c.sound()