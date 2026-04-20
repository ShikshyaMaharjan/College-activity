filename = "file.bin"
size = int(input("Enter chunk size: "))

with open(filename, "rb") as f:
    while chunk := f.read(size):
        print(chunk)
        