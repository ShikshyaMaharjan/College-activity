list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]
i = 0
common = [] 
while i < len(list1):
    if list1[i] in list2:
        common += [list1[i]]  
    i += 1
else:
    if common:
        print("Common elements are:", common)
    else:
        print("No common elements found")
