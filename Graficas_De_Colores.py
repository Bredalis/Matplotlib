
# Librerias

import matplotlib.pyplot as plt
import numpy as np

def diagrama_de_puntos():

	# Grafica

	fig, grafica = plt.subplots(subplot_kw = dict(projection = "polar"))

	# Datos para graficar

	matriz = np.linspace(0, 2, 20)
	colores = np.pi * matriz

	# Grafica circular

	visualizacion = grafica.scatter(colores, matriz, 
		c = colores, s = 100, cmap = "hsv")
	plt.colorbar(mappable = visualizacion, location = "left")

diagrama_de_puntos()

# Datos para graficar

matriz = np.arange(36).reshape(6, 6)

# Mostrar una grafica de colores a partir de la matriz

plt.imshow(
	matriz, cmap = plt.cm.winter,
	interpolation = "bilinear", extent = [1, 10, 1, 10])

plt.show()