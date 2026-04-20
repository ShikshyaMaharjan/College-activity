class TicketBooth:
    def __init__(self):
        self.people = 0
        self.amount = 0
        self.tickets = 0   # fixed here

    def no_sales(self):
        self.people += 1

    def sale(self):
        self.people += 1
        self.tickets += 1
        self.amount += 2.5

    def display_all(self):
        print("People visited:", self.people)
        print("Tickets sold:", self.tickets)
        print("Total amount:", self.amount)

    def display_sales(self):
        print("Tickets sold:", self.tickets)
        print("Amount:", self.amount)


t = TicketBooth()
t.sale()
t.sale()
t.no_sales()
t.display_all()
t.display_sales()