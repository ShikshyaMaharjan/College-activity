class Person:
    def __init__(self, name):
        self.name = name
class Teacher:
    def __init__(self, subject):
        self.subject = subject
class Tutor(Person, Teacher):
    def __init__(self, name, subject):
        Person.__init__(self, name)
        Teacher.__init__(self, subject)
    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
t = Tutor("Ram", "Python")
t.display()