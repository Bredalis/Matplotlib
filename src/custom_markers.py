
# Libraries
import matplotlib.pyplot as plt
import numpy as np


# Plot size
fig, ax = plt.subplots(figsize=(5, 5))

# Data
x = np.arange(6)
y = x

# Line plot with custom markers
ax.plot(
    x, y, marker="D",
    markerfacecolor="pink", markeredgecolor="k",
    fillstyle="left", markersize=20,
    markerfacecoloralt="green"
)

plt.show()
