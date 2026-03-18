a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("\n-- Calculate Menu")
print("1. Add")
print("2. Sub")
print("3. Multiply")
print("4. Divide")
choice=int(input("Enter Your Choice:"))

match choice:
    case 1:
        print("Sum =",a+b)
    case 2:
        print("Subtract =", a-b)
    case 3:
        print("product =", a*b)
    case 4:
        print("Division =" ,a/b)
    case _:
        print("Invalid Choice!!")