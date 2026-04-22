numbers = [1, 2, 2, 3, 4, 4, 5]
#set(numbers) converts the list into a set, which automatically removes duplicates because sets cannot have repeated elements.
unique = list(set(numbers))
print("Without duplicates:", unique)