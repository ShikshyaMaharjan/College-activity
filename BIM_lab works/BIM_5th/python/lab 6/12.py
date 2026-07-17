class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
s = Square(5)
c = Circle(3)
print("Square Area:", s.area())
print("Circle Area:", c.area())