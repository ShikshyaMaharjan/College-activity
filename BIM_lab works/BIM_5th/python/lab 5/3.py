class Triangle:
    def __init__(self):
        self.base=0
        self.height=0
    def getdata(self):
        self.base=float(input("Enter the base:" ))
        self.height=float(input("Enter the height: "))
    def calcarea(self):
        return 0.5*self.base*self.height
    def display(self):
        print("Base: ",self.base)
        print("Height: ",self.height)
        print("Area: ",self.calcarea())  
t=Triangle()
t.getdata()
t.display()
              
