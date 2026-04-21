import matplotlib.pyplot as plt
import numpy as np

# Continuous data
data = np.random.randint(1, 100, 50)

# Subplot 1: Scatter plot
x = [1, 2, 3, 4, 5]
y = [5, 3, 6, 2, 9]

plt.subplot(1, 3, 1)
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")

# Subplot 2: Histogram
plt.subplot(1, 3, 2)
plt.hist(data, color='blue')
plt.title("Histogram")

# Subplot 3: Box plot
plt.subplot(1, 3, 3)
plt.boxplot(data)
plt.title("Box Plot")

plt.tight_layout()
plt.show()