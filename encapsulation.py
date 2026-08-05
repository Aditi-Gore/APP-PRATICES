class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks      # Private variable

    # Getter Method
    def get_marks(self):
        return self.__marks

    # Setter Method
    def set_marks(self, marks):
        self.__marks = marks

# Creating Object
s = Student("Aditi", 85)

# Accessing Private Data using Getter
print("Name:", s.name)
print("Marks:", s.get_marks())

# Modifying Private Data using Setter
s.set_marks(95)
print("Updated Marks:", s.get_marks())