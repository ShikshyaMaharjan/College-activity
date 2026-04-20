with open("file.bin", "rb") as f1:
    data1 = f1.read()

with open("data.bin", "rb") as f2:
    data2 = f2.read()

with open("merged.bin", "wb") as f3:
    f3.write(data1 + b"\n" + data2)

print("Merged successfully")