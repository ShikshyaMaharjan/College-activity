data = ["Luniva", "Aarya", "Nikisha","Apple", "Banana","Mango","Pineapple","Papaya"]

with open("data.txt", "w") as f:
    for item in data:
        f.write(item + "\n")

print("Written successfully")