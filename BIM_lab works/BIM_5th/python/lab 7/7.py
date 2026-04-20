filename = "file.txt"

line_no = int(input("Enter line number: "))

with open(filename, "r") as f:
    lines = f.readlines()

if line_no <= len(lines):
    print(lines[line_no - 1])
else:
    print("Line not found")