class Box:
    def readValues(self):
        self.width=int(input("Enter width: "))
        self.height=int(input("Enter height: "))
        self.depth=int(input("Enter depth: "))
    def area(self):
        return self.width*self.height
    def volume(self):
        return self.width*self.height*self.depth
b=Box()
b.readValues()
print("Area: ",b.area())
print("Volume: ",b.volume())