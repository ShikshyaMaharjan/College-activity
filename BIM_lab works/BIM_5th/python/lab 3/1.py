def calc(a,b):
    print("Add:",a+b)
    print("Sub:",a-b)
    print("Mul:",a*b)
    print("Div:",a/b)
    
    if type(a) !=complex and type(b) != complex:
        print("Floor div:",a/b)
calc(12,3)
calc(12.5,1.5)
calc(2+3j,1+1j)