import numpy as np

arr = np.random.randint(1, 101, 20)

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Std Dev:", np.std(arr))
print("Variance:", np.var(arr))
print("Sum:", np.sum(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))
print("25th percentile:", np.percentile(arr, 25))
print("75th percentile:", np.percentile(arr, 75))