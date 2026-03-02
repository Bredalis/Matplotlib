
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator


def bar_chart():
    fig, ax = plt.subplots()

    # Bar chart data
    df = pd.DataFrame({
        "Subjects": 
        ["English", "Math", "History", "Language", "Physics", "Biology"],
        "Quantities": [6, 5, 4, 7, 5, 6]
    })

    ax.bar(df["Subjects"], df["Quantities"], color="skyblue")
    ax.grid(axis="y")

    # Major and minor ticks on y-axis
    ax.set_yticks(range(0, 11, 2))
    ax.set_yticks(np.arange(0, 10.5, 0.5), minor=True)

    # Y-axis limits
    ax.set_ylim(0, 10)

    # Location and format of y-axis divisions
    ax.yaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_formatter("{x:.1f} points")

    # Label size and rotation configuration
    ax.tick_params(axis="y", which="major", labelsize=14)
    ax.tick_params(axis="x", which="major", labelsize=14, rotation=15)


# Create line chart with logarithmic scale
fig, ax = plt.subplots()

# Line chart data
x = np.linspace(0, 20, 200)
y = x ** 3

ax.plot(x, y, label="x^3")

# Y-axis scale and limits
ax.set_yscale("log")
ax.set_ylim(0, 100000)

# Custom x-axis labels
ax.set_xticks(np.arange(0, 20, 4))
ax.set_xticklabels(["Android", "SQL", "Linux", "Windows", "Mac"])

bar_chart()
plt.show()
