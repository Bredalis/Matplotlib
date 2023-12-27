
# Librerias

import matplotlib.pyplot as plt
import numpy as np

# Datos para graficar

matriz = np.arange(36).reshape(6, 6)

def Diagrama_De_Puntos():

	# Grafica

	fig, grafica = plt.subplots(subplot_kw = dict(projection = 'polar'))

	# Datos para graficar

	matriz = np.linspace(0, 2, 20)
	colores = np.pi*matriz

	# Grafica circular

	visualizacion = grafica.scatter(colores, matriz, 
		c = colores, s = 100, cmap = 'hsv')
	plt.colorbar(mappable = visualizacion, location = 'left')

# Mostrar una grafica de colores a partir de la matriz

plt.imshow(
	matriz, cmap = plt.cm.winter,
	interpolation = 'bilinear', extent = [1, 10, 1, 10])

Diagrama_De_Puntos()

plt.show()