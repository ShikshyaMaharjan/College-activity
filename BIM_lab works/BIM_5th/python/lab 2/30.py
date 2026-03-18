
numbers = eval(input("Enter a list of numbers: "))

for num in numbers:
    if num < 0:
        break  
    print(num)