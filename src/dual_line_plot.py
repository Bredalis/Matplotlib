
import matplotlib.pyplot as plt
import numpy as np


# Data
x = np.linspace(0, 20, 10)
y = x ** 2
x_2 = np.linspace(21, 30, 10)
y_2 = x_2 ** 2

# Two lines
plt.plot(x, y, "rd-", label="Red Line")
plt.plot(x_2, y_2, "ko:", label="Black Line")

# Background grid lines
plt.grid(axis="y", color="b", which="major", alpha=0.5, linestyle="--")
plt.grid(axis="x", color="b", which="major", alpha=0.2, linestyle="--")

# Axis label size and legend
plt.tick_params(axis="y", which="major", labelsize=15)
plt.legend()
plt.show()
