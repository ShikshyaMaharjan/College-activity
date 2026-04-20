data = b"Hello Binary"

with open("file.bin", "wb") as f:
    f.write(data)

print("Written")