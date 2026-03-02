
import matplotlib.pyplot as plt
import numpy as np


# Simple line plot
x_axis = ["A", "B", "C", "D", "E"]
y_axis_1 = [10, 20, 30, 40, 50]
y_axis_2 = [20, 30, 40, 50, 60]

plt.plot(x_axis, y_axis_1)
plt.plot(x_axis, y_axis_2)
plt.show()

# Data for complex plots
years = list(range(2011, 2021))
level_1 = np.random.rand(10) * 100
level_2 = np.random.rand(10) * 200 + 100
level_3 = np.random.rand(10) * 300 + 200
level_4 = np.random.rand(10) * 400 + 300
level_5 = np.random.rand(10) * 500 + 400

levels = [level_1, level_2, level_3, level_4, level_5]
colors = ["purple", "pink", "blue", "brown", "black"]
markers = ["<", ">", "*", ".", "+"]
styles = ["-", "--", ":", "-.", " "]

# Line plot with style variations
for i in range(5):
    plt.plot(
        years, levels[i], label=f"Level {i + 1}",
        color=colors[i], marker=markers[i], linestyle=styles[i]
    )

plt.legend()
plt.title("Certification Exam")
plt.xlabel("Years")
plt.ylabel("Score")
plt.yticks(np.arange(0, 1001, 50))
plt.grid()
plt.minorticks_on()
plt.show()

# Vertical bar chart
x = np.arange(10)
offsets = [0.0, 0.2, 0.4, 0.6, 0.8]

for i in range(5):
    plt.bar(x + offsets[i], levels[i], label=f"Level {i + 1}", width=0.2)
plt.legend()
plt.show()

# Horizontal bar chart
for i in range(5):
    plt.barh(x + offsets[i], levels[i], label=f"Level {i + 1}", height=0.2)
plt.legend()
plt.show()

# Stacked bar chart
plt.bar(x, level_5, label="Level 1", bottom=level_2 + level_3 + level_4 + level_5)
plt.bar(x, level_4, label="Level 2", bottom=level_3 + level_4 + level_5)
plt.bar(x, level_3, label="Level 3", bottom=level_4 + level_5)
plt.bar(x, level_2, label="Level 4", bottom=level_5)
plt.bar(x, level_1, label="Level 5")
plt.legend()
plt.show()

# Scatter plot
for i in range(5):
    plt.scatter(x, levels[i], label=f"Level {i + 1}")
plt.legend()
plt.show()

# Pie chart
plt.pie(
    level_1,
    labels=["Cherry", "Orange", "Grape", "Strawberry", "Pear", "Lemon",
            "Banana", "Tamarind", "Coconut", "Pineapple"]
)
plt.show()
