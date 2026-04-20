with open("file1.txt", "w") as f:
    for i in range(1, 101):
        f.write(str(i) + "\n")

print("Written successfully")