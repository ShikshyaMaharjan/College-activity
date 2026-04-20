class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b
c=Calculator(10,5)
print("Add: ",c.addition())
print("Sub: ",c.subtraction())
print("Multiply: ",c.multiplication())
print("Division: ",c.division())
    