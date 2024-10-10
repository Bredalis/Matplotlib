
# Librerías

import matplotlib.pyplot as plt
import numpy as np

# Datos Normales

datos = np.random.normal(size = 100000)

plt.hist(datos, color = "pink", ec = "black")
plt.title("Distribucion Normal")
plt.show()

# Uniforme

datos = np.random.uniform(size = 100000)

plt.hist(datos, color = "skyblue", ec = "black")
plt.title("Distribucion Uniforme")
plt.show()

# Exponenciales

datos = np.random.exponential(size = 100000)

plt.hist(datos, color = "green", ec = "black")
plt.title("Distribucion Exponencial")
plt.show()