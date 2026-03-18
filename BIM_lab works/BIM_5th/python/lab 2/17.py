
n = int(input("Enter how many numbers you want to input: "))

total = 0

for i in range(1, n + 1):
    num = float(input(f"Enter number {i}: "))
    total += num

average = total / n

print("Sum of the numbers:", total)
print("Average of the numbers:", average)