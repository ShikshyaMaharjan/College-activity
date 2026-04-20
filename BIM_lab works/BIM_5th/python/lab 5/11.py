class Student:
    def __init__(self, id=100, marks=50.0):
        self.id = id
        self.marks = marks

    @classmethod
    def from_object(cls, obj):
        return cls(obj.id, obj.marks)

    def display(self):
        print(f"ID: {self.id} Marks: {self.marks}")


# Default constructor
s1 = Student()
print("Default constructor called")
s1.display()

# Parameterized constructor
s2 = Student(101, 85.5)
print("Parameterized constructor called")
s2.display()

# Copy constructor
s3 = Student.from_object(s2)
print("Copy constructor called")
s3.display()