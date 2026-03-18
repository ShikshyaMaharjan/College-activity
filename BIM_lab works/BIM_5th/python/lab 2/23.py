total = 0
for i in range(101, 200):
    if i % 7 == 0 and i % 5 != 0:
        total += i
print("Sum of numbers divisible by 7 but not by 5:", total)