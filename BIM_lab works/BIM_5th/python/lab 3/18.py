lst = [10, 20, 30]
print("Original list:", lst)

lst.append(40)
print("Appended:", lst)

lst.insert(1, 15)
print("Inserted:", lst)

lst.remove(30)
print("Removed:", lst)

lst.pop()
print("Popped:", lst)

del lst[0]
print("Deleted:", lst)