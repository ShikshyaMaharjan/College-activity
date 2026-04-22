import copy

list1 = [[1, 2], [3, 4]]

# Shallow copy
shallow_copy = list1.copy()

# Deep copy
deep_copy = copy.deepcopy(list1)

print("Original:", list1)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)