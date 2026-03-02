
"""Polynomial line chart with multiple power functions."""

import matplotlib.pyplot as plt
import numpy as np


def create_polynomial_chart():
    """Create a line chart displaying x, x², and x³ functions."""
    # Data
    x = np.linspace(0, 2, 100)

    # Chart size and layout configuration
    plt.figure(figsize=(5, 3), layout="constrained")

    # Line plots
    plt.plot(x, x, label="Blue Line")
    plt.plot(x, x ** 2, label="Orange Line")
    plt.plot(x, x ** 3, label="Green Line")

    # Titles and labels
    plt.title("Theme")
    plt.xlabel("X Label")
    plt.ylabel("Y Label")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    create_polynomial_chart()
