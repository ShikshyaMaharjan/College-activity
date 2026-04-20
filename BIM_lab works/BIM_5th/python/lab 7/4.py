data = {"Name": "Aarya", "Age": 20, "Faculty": "BIM"}

with open("file1.txt", "w") as f:
    for k, v in data.items():
        f.write(k + ": " + str(v) + "\n")

print("Written successfully")