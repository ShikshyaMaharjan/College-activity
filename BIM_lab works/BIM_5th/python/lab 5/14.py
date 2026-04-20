class TicketBooth:
    def __init__(self):
        self.people=0
        self.amount=0
    def buy_ticket(self):
        self.people+=1
        self.amount+=2.5
    def no_ticket(self):
        self.people+=1
    def display(self):
        print("People visited: ",self.people)
        print("Total amount: ",self.amount)
t=TicketBooth()
t.buy_ticket()
t.no_ticket()
t.buy_ticket()
t.display()