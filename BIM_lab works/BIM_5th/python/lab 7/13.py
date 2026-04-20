data = [{"a": 1}, {"b": 2}, {"c": 3}]

with open("data.bin", "wb") as f:
    for item in data:
        line = str(item) + "\n"
        f.write(line.encode())

print("Written")