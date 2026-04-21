import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

print("Original array:")
print(arr)

# access 2nd row 3rd column
print("Element:", arr[1,2])

# modify element
arr[1,2] = 99

print("After modification:")
print(arr)