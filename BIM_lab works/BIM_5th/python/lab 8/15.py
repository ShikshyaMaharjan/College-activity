import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

# Create figure with 2 subplots
plt.subplot(1, 2, 1)
plt.plot(x, y, marker='o', color='blue')
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.scatter(x, y, marker='s', color='red')
plt.title("Scatter Plot")

plt.show()