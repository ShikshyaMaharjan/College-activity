class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side
class Rectangle(Square):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
s = Square(5)
print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())
r = Rectangle(8, 4)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())