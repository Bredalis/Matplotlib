
import matplotlib.pyplot as plt
import numpy as np


# Plot configuration
fig, ax = plt.subplots()

# Data
x = np.linspace(0.1, 6)
y = np.sin(x)

# Stem plot
ax.stem(x, y, linefmt="k:", markerfmt="D", basefmt="C3--")

# Axis configuration
ax.spines["left"].set_color("blue")
ax.spines["right"].set_color("red")
ax.spines["left"].set_linewidth(1)
ax.spines["right"].set_linewidth(1)
ax.spines["left"].set_alpha(0.5)
ax.spines["right"].set_alpha(0.5)
ax.spines["left"].set_linestyle("dashed")
ax.spines["right"].set_linestyle("dashed")
ax.spines["left"].set_visible(True)
ax.spines["right"].set_visible(True)

# Background grid
ax.grid(True, linewidth=1)
plt.show()
