import numpy as np
arr3d=np.arange(27).reshape(3,3,3)
sub=arr3d[1,:,:]
sub=sub*2
print("Mean:",np.mean(sub))