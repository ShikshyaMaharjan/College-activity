class Sort:
    def getdata(self):
        self.arr = list(map(int, input("Enter numbers: ").split()))
    
    def sorting(self):
        self.arr.sort()
    
    def display(self):
        print("Sorted:", self.arr)

s = Sort()
s.getdata()
s.sorting()
s.display()