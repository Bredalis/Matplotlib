
import matplotlib.pyplot as plt
import numpy as np


# Data for scatter plot and line
x = np.arange(8)
y = [3, 1, 1, 2, 5, 5, 7, 6]


def bar_chart():
    fig, ax = plt.subplots()

    # Bar chart data
    emotions = ["Joy", "Anger", "Sadness", "Fear", "Disgust"]
    count = [16, 5, 7, 10, 14]

    ax.bar(emotions, count, color="aqua")
    ax.set_title("Abstract Nouns")


# Create figure and axes for scatter and line
fig, ax = plt.subplots()

# Scatter plot (circles)
ax.scatter(x, y, s=200, color="#ff0345", edgecolor="k", label="Points")

# Line plot
ax.plot(x, y, color="blue", linewidth=5, zorder=0, label="Line")
ax.set_title("Scatter and Line Plot")
ax.legend()

# Create a second simple figure
fig, ax2 = plt.subplots()
ax2.plot([1, 2, 3, 4], [1, 2, 4, 3], color="purple", marker="o")
ax2.set_title("First Simple Plot")

bar_chart()
plt.show()
