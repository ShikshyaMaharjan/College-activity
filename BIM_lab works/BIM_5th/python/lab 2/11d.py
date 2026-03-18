a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))
smallest = a if a < b and a < c else b if b < c else c
print("Smallest number is:", smallest)