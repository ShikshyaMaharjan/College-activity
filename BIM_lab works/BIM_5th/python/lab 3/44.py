import copy

a = {10, 20, 30, 40}

deep_copy = copy.deepcopy(a)

print("Original set:", a)
print("Deep copy:", deep_copy)