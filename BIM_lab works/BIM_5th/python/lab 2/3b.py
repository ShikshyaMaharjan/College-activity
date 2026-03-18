num=input("Enter a 4-digit number:")
sum_digits=0
for digit in num:
    sum_digits += int(digit)
print("sum of digits:",sum_digits)