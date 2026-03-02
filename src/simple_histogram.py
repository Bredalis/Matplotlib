
import matplotlib.pyplot as plt


# Data for histogram
data = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create histogram
plt.hist(data, color="pink", edgecolor="black", bins=5)
plt.show()
