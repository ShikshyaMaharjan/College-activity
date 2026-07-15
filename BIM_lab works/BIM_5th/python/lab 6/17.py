class Publication:
    def __init__(self):
        self.title = ""
        self.price = 0
    def getdata(self):
        self.title = input("Enter title: ")
        self.price = float(input("Enter price: "))
    def putdata(self):
        print("Title:", self.title)
        print("Price:", self.price)
class Book(Publication):
    def __init__(self):
        super().__init__()
        self.page = 0
    def getdata(self):
        super().getdata()
        self.page = int(input("Enter number of pages: "))
    def putdata(self):
        super().putdata()
        print("Pages:", self.page)
class CDROM(Publication):
    def __init__(self):
        super().__init__()
        self.playtime = 0
    def getdata(self):
        super().getdata()
        self.playtime = float(input("Enter playtime (minutes): "))
    def putdata(self):
        super().putdata()
        print("Playtime:", self.playtime, "minutes")
print("Book Details")
b = Book()
b.getdata()
print("\nCDROM Details")
c = CDROM()
c.getdata()
print("\nBook Information")
b.putdata()
print("\nCDROM Information")
c.putdata()