ages = eval(input("Enter ages of 10 people in list form: "))

count = 0
for age in ages:
    if 25 <= age <= 50:
        count += 1

print("The number of people aged between 25 and 50 is", count)


    