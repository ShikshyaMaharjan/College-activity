import numpy as np

# Create 1D array of random integers
arr = np.random.randint(1, 50, 10)

print("Original array:", arr)

# Sort in ascending order
arr_sorted = np.sort(arr)

print("Sorted array:", arr_sorted)

# Reshape into 2D array (2 rows, 5 columns)
arr_2d = arr_sorted.reshape(2, 5)

print("2D array:")
print(arr_2d)