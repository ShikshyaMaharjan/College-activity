with open("poem.txt", "w") as f:
    f.write("Roses are red\n")
    f.write("Violets are blue\n")
    f.write("Coding is fun\n")
    f.write("Python is cool\n")

print("File created")
with open("poem.txt", "r") as f:
    text = f.read()   # read full file

    f.seek(0)         # move pointer back to beginning

    lines = text.split("\n")

    for line in reversed(lines):
        print(line)