
# Librerias

import matplotlib.pyplot as plt
import numpy as np

# Datos normales

datos = np.random.normal(size = 100000)

# Histograma

plt.hist(datos, color = "pink", ec = "black")
plt.title("Distribucion Normal")
plt.show()

# Datos uniforme

datos = np.random.uniform(size = 100000)

# Histograma

plt.hist(datos, color = "skyblue", ec = "black")
plt.title("Distribucion Uniforme")
plt.show()

# Datos exponenciales

datos = np.random.exponential(size = 100000)

# Histograma

plt.hist(datos, color = "green", ec = "black")
plt.title("Distribucion Exponencial")
plt.show()