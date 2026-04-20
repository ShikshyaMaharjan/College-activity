with open("file2.txt", "r") as f:
    text = f.read()

words = text.split()
print("Total words:", len(words))