
import matplotlib.pyplot as plt
import pandas as pd


# Load data
people = pd.read_csv("../csv/people.csv")
print(people)


def scatter_plot(x, y):
    """Function to plot scatter between two variables."""
    plt.scatter(people[x], people[y])

    # Label configuration
    x_label = x.capitalize()
    y_label = y.capitalize()

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f"{x_label} and {y_label}")
    plt.show()


# Scatter plots between different pairs of data
scatter_plot("height", "weight")
scatter_plot("income", "hours_worked")
scatter_plot("income", "absences")

# Correlation matrix
matrix = people.corr()

plt.matshow(matrix, cmap="bwr", vmin=-1, vmax=1)
plt.xticks(range(len(people.columns)), people.columns, rotation=90)
plt.yticks(range(len(people.columns)), people.columns)

# Show values inside correlation matrix
for i in range(len(matrix.columns)):
    for j in range(len(matrix.columns)):
        plt.text(i, j, round(matrix.iloc[i, j], 2),
                 ha="center", va="center")

plt.colorbar()
plt.show()
