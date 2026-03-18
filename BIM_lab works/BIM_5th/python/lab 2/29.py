# Sample list input
my_list = [1, 20, 3, 4, 5, 20]

i = 0
while i < len(my_list):
    if my_list[i] in my_list[i+1:]:
        print("Duplicates found")
        break
    i += 1
else:
    # This else executes only if the while loop completes normally (no break)
    print("No duplicates")