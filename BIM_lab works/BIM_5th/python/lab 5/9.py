class Box:
    def __init__(self,w,h,d):
        self.w=w
        self.h=h
        self.d=d
    def area(self):
        return self.w*self.h
    def volume(self):
        return self.w*self.h*self.d
b=Box(2,3,4)
print("Area : ",b.area())
print("Volume: ",b.volume())

    