import numpy as np
arr3d=np.arange(27).reshape(3,3,3)
slice2d = arr3d[0]
print(slice2d)
print("Dimensions:",slice2d.ndim)