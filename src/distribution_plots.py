
# Libraries
import matplotlib.pyplot as plt
import numpy as np


# Generate and plot normal distribution data
normal_data = np.random.normal(size=100000)
plt.hist(normal_data, color="pink", edgecolor="black")
plt.title("Normal Distribution")
plt.show()

# Generate and plot uniform distribution data
uniform_data = np.random.uniform(size=100000)
plt.hist(uniform_data, color="skyblue", edgecolor="black")
plt.title("Uniform Distribution")
plt.show()

# Generate and plot exponential distribution data
exponential_data = np.random.exponential(size=100000)
plt.hist(exponential_data, color="green", edgecolor="black")
plt.title("Exponential Distribution")
plt.show()
