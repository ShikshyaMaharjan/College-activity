data = {"name": "Shikshya", "age": 20}

file = open("data.bin", "wb")

text = str(data)        # object → string
binary = text.encode()  # string → bytes

file.write(binary)
file.close()