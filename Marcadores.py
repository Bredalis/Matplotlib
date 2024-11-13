
# Librerías
import matplotlib.pyplot as plt
import numpy as np

# Tamaño de la gráfica
fig, grafica = plt.subplots(figsize = (5, 5))

# Datos
x = np.arange(6)
y = x

# Gráfica lineal con marcadores personalizados
grafica.plot(
    x, y, marker = "D",
    markerfacecolor = "pink", markeredgecolor = "k",
    fillstyle = "left", markersize = 20,
    markerfacecoloralt = "green"
)

plt.show()