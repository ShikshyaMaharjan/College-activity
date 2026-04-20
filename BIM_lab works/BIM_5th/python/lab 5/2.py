class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getdata(self):
        self.radius=float(input("Enter radius: "))
    def calcarea(self):
        return 3.14*self.radius*self.radius
    def display(self):
        print("Area: ",self.calcarea())
c= Circle(0)
c.getdata()
c.display()