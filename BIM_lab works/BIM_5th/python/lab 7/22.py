# Step 1: Write data into file
with open("grades.txt", "w") as f:
    for i in range(10):
        name = input("Enter student name: ")
        marks = input("Enter 5 subjects marks: ")
        f.write(name + "," + marks + "\n")

print("Data saved")

# Step 2: Read and process data
with open("grades.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")

        name = data[0]
        marks = list(map(int, data[1:]))

        avg = sum(marks) / 5

        if avg > 50:
            print(name)