class Sphere:
    def getdata(self):
        self.r=float(input("Enter radius: "))
    def area(self):
        return 4*3.14*self.r*self.r
    def volume(self):
        return (4/3)*3.14*self.r**3
    def display(self):
        print("Area: ",self.area())
        print("Volume: ",self.volume())
s=Sphere()
s.getdata()
s.display()