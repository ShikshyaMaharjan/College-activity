with open("employees.txt", "w") as f:
    n = int(input("Enter number of employees: "))

    for i in range(n):
        name = input("Name: ")
        salary = input("Salary: ")

        f.write(name + ","  + salary + "\n")

print("File created")
total = 0

with open("employees.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        total += int(data[1])   # salary is assumed at index 3

with open("total_salary.txt", "w") as f:
    f.write("Total Salary: " + str(total))

print("Total salary calculated and saved")