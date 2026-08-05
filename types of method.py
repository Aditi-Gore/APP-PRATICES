class Student:
    # Class Variable
    college = "MIT ADT University"

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    # Class Method
    @classmethod
    def show_college(cls):
        print("College Name:", cls.college)

    # Static Method
    @staticmethod
    def greet():
        print("Welcome to Python Programming!")

# Creating Object
s1 = Student("Aditi", 20)

# Calling Instance Method
print("Instance Method:")
s1.display()

# Calling Class Method
print("\nClass Method:")
Student.show_college()

# Calling Static Method
print("\nStatic Method:")
Student.greet()