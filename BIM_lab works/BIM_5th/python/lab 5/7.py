class Number:
    def input(self):
        self.a=int(input("Enter first number: "))
        self.b=int(input("Enter second number: "))
        self.c=int(input("Enter three number: "))
    def largest(self):
        return max(self.a,self.b,self.c)
    def display(self):
        print("Largest number: ",self.largest())
n=Number()
n.input()
n.display()
