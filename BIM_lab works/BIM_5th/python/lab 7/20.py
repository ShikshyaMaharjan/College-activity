n = int(input("Enter number of employees: "))

with open("employeeinfo.txt", "w") as f:
    for i in range(n):
        name = input("Name: ")
        eid = input("ID: ")
        office = input("Office name: ")
        job = input("Occupation: ")
        f.write(name + "," + eid + "," + office + "," + job + "\n")

print("Records saved")

# Display employees from NCCS College
with open("employeeinfo.txt", "r") as f:
    print("\nEmployees from NCCS College:")
    for line in f:
        data = line.strip().split(",")
        if data[2] == "Nccs College":
            print(data[0])