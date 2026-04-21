import matplotlib.pyplot as plt
# Dataset for scatter plot (different data)
x2 = [1, 2, 3, 4, 5]
y2 = [5, 3, 6, 2, 9]
# Categorical data for bar graph
subjects = ["Math", "CS", "Physics", "English"]
marks = [80, 90, 70, 85]
# Subplot 2: Scatter plot (different dataset)
plt.subplot(1, 2, 1)
plt.scatter(x2, y2, marker='s', color='red')
plt.title("Scatter Plot")

# Subplot 3: Bar graph
plt.subplot(1, 2, 2)
plt.bar(subjects, marks, color=['green', 'blue', 'orange', 'purple'])
plt.title("Bar Graph")

plt.tight_layout()
plt.show()