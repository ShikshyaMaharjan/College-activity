import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.plot(x, y, marker='o', color='blue')

# Labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Line Plot")

# Grid lines
plt.grid(True, linestyle='--', color='gray')

plt.show()