
# Librerías
import matplotlib.pyplot as plt
import numpy as np

# Generar y graficar datos normales
datos_normales = np.random.normal(size = 100000)
plt.hist(datos_normales, color = "pink", edgecolor = "black")
plt.title("Distribución Normal")
plt.show()

# Generar y graficar datos uniformes
datos_uniformes = np.random.uniform(size = 100000)
plt.hist(datos_uniformes, color = "skyblue", edgecolor = "black")
plt.title("Distribución Uniforme")
plt.show()

# Generar y graficar datos exponenciales
datos_exponenciales = np.random.exponential(size = 100000)
plt.hist(datos_exponenciales, color = "green", edgecolor = "black")
plt.title("Distribución Exponencial")
plt.show()