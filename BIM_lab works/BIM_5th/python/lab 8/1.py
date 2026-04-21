import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr = arr.astype(np.float32)
arr2d = arr.reshape(2,5)

print(arr2d)