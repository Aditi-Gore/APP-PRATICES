# Class Definition
class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

# Creating Objects
obj1 = Student("Aditi", 20)
obj2 = Student("Rahul", 21)

# Calling Method
obj1.display()
print()
obj2.display()