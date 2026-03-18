import copy 
original =[[1,2],[3,4]]
shallow_copy=copy.copy(original)
deep_copy=copy.deepcopy(original)
shallow_copy[0][0]=99
deep_copy[1][1]=88
print("Original:",original)
print("Shallow copy:",shallow_copy)
print("Deep copy:",deep_copy)