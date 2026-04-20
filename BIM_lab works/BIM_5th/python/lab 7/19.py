n = int(input("Enter number of colleges: "))

with open("university.txt", "w") as f:
    for i in range(n):
        name = input("Name: ")
        location = input("Location: ")
        faculty = input("No of faculties: ")
        f.write(name + ","+"Address:" + location + ","+"Faculty no:" + faculty + "\n")

print("Records saved")

# Display records
with open("university.txt", "r") as f:
    print("\nCollege Records:")
    for line in f:
        print(line.strip())