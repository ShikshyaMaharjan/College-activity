import matplotlib.pyplot as plt

# Data
labels = ["Math", "CS", "Physics", "English"]
marks = [80, 90, 70, 85]

# Colors for each slice
colors = ["gold", "lightblue", "lightgreen", "pink"]

# Explode (separate one slice slightly)
explode = [0, 0.1, 0, 0]

# Pie chart
plt.pie(marks, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%')

plt.title("Subject Marks Distribution")

plt.show()
