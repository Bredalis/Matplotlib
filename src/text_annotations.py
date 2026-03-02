
import matplotlib.pyplot as plt


# Lines
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], label="Blue Line")
plt.plot([1, 2, 3, 4], [1, 4, 3, 2], label="Orange Line")

# Points
plt.scatter([1, 2, 3, 4], [4, 3, 2, 1], label="Points")

# Text at specific location
plt.text(
    x=2.5, y=2.5, s="Text Location",
    fontsize=10, color="green",
    bbox=dict(
        facecolor="pink", edgecolor="#003430",
        alpha=0.8, boxstyle="larrow"
    )
)

# Annotation with arrow
plt.annotate(
    "New Text", xy=(1.3, 2), xytext=(2, 1),
    arrowprops=dict(arrowstyle="simple",
                    facecolor="yellow", edgecolor="k")
)

# Legend
plt.legend(loc="upper center", shadow=False,
           fontsize="x-large", facecolor="pink")
plt.show()
