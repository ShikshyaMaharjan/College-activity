with open("data.txt", "r") as f:
    lines = f.readlines()

for i in range(4, 6):
    print(lines[i].strip())

