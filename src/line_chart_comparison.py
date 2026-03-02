"""Line chart comparison with two data series."""


import matplotlib.pyplot as plt


def create_line_chart():
    """Create a line chart comparing two data series."""
    # Data
    x = range(12)
    x_2 = range(13)
    y = [
        20340, 21033, 21440, 22509, 23887, 21490,
        22400, 24943, 23098, 23450, 26900, 28034
    ]
    y_2 = [
        20340, 21033, 21440, 22509, 23887, 21490,
        22400, 24943, 23098, 23450, 26900, 28034, 24890
    ]

    # Available chart styles
    print(f"Styles: {plt.style.available}")

    # Apply chart style
    plt.style.use("seaborn-v0_8-bright")

    # Line plots
    plt.plot(
        x, y,
        color="k",
        linestyle="dotted",
        marker="p",
        label="Black Line"
    )
    plt.plot(
        x_2, y_2,
        color="b",
        linestyle="dotted",
        marker="o",
        label="Blue Line"
    )

    # Axis and label configuration
    plt.xticks(x)
    plt.tick_params(axis="both", width=1, top=True, right=True)
    plt.title("Theme")
    plt.xlabel("X Label")
    plt.ylabel("Y Label")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    create_line_chart()
