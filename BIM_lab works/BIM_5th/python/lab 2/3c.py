num = input("Enter a 4-digit number: ")  # take input from user
reverse = ""

for digit in num:
    reverse = digit + reverse

print("Reverse of the number:", reverse)
