text = input("Enter a string: ")

mid = len(text) // 2

if len(text) % 2 == 0:
    print(text[mid-1:mid+1])
else:
    print(text[mid])