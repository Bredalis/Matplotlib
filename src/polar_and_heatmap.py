
import matplotlib.pyplot as plt
import numpy as np


def polar_scatter():
    fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))

    # Data
    r = np.linspace(0, 2, 20)
    theta = np.pi * r

    # Polar scatter plot
    scatter = ax.scatter(theta, r, c=theta, s=100, cmap="hsv")
    plt.colorbar(mappable=scatter, location="left")


polar_scatter()

# Data for color matrix
matrix = np.arange(36).reshape(6, 6)

# Display color plot from matrix
plt.imshow(
    matrix, cmap="winter", interpolation="bilinear",
    extent=[1, 10, 1, 10]
)
plt.show()
