class Rectangle:
    def readdata(self):
        self.length=float(input("Enter length:"))
        self.breadth=float(input("Enter breadth:"))
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def display(self):
        print("Area: ",self.area())
        print("Perimeter: ",self.perimeter())
r=Rectangle()
r.readdata()
r.display()
