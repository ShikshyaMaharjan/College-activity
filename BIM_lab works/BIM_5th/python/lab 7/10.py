filename = "file2.txt"
word = input("Enter word to search: ")

with open(filename, "r") as f:
    text = f.read()

print("Occurrences:", text.count(word))