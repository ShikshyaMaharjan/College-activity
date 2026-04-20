class IntAmount:
    def getdata(self):
        self.principal=float(input("Enter principle: "))
        self.rate=float(input("Enter rate: "))
        self.time=int(input("Enter time: "))
    def interest(self):
        return (self.principal*self.rate*self.time)/100
    def amount(self):
        return self.principal+self.interest()
obj=IntAmount()
obj.getdata()
print("Interest: ",obj.interest())
print("Amount: ",obj.amount())

