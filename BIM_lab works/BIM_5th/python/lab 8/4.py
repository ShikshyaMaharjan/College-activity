import numpy as np
arr=np.array([1,2,3,4])
view=arr.view()
copy=arr.copy()
view[0]=100
copy[1]=200
print("Original:",arr)
print("View:",view)
print("Copy:",copy)
