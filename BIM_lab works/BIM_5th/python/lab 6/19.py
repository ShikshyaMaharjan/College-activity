class Student:
    def read_roll(self):
        self.roll = int(input("Enter Roll No: "))
    def display_roll(self):
        print("Roll No:", self.roll)
class Test(Student):
    def read_marks(self):
        self.mark1 = float(input("Enter marks of Subject 1: "))
        self.mark2 = float(input("Enter marks of Subject 2: "))
    def display_marks(self):
        print("Subject 1 Marks:", self.mark1)
        print("Subject 2 Marks:", self.mark2)
class Result(Test):
    def calculate_total(self):
        self.total = self.mark1 + self.mark2
    def display_total(self):
        print("Total Marks:", self.total)
r = Result()
r.read_roll()
r.read_marks()
r.calculate_total()
print("\nStudent Result")
r.display_roll()
r.display_marks()
r.display_total()