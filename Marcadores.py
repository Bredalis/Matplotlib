
# Librerias

import matplotlib.pyplot as plt
import numpy as np

# Tamaño de la grafica

fig, grafica = plt.subplots(figsize = (5, 5))

# Datos para graficar

x = np.arange(6)
y = x

# Grafica lineal

grafica.plot(
	x, y, marker = "D",
	markerfacecolor = "pink", markeredgecolor = "k",
	fillstyle = "left", markersize = 20,
	markerfacecoloralt = "green")

plt.show()