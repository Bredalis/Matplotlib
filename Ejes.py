
# Librerías

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import pandas as pd
import numpy as np

# Creacion de la grafica

fig, grafica = plt.subplots()

# Datos

x = np.linspace(0, 20, 200)
y = x ** 3

def diagrama_de_barras():

	fig, grafica = plt.subplots()

	df = pd.DataFrame({
		"Campos": ["Ingles", "Matematica", "Historia", 
		"Lengua", "Fisica", "Biologia"],
		"Cantidades": [6, 5, 4, 7, 5, 6]
	})

	# Barras

	grafica.bar(df.Campos, df.Cantidades)
	grafica.grid(axis = "y")

	# Etiquetas mayores y menores

	grafica.set_yticks(range(0, 11, 2))
	grafica.set_yticks(range(0, 11, 2), minor = 1)

	# Limite de y

	grafica.set(ylim = (0, 10))

	# Ubicacion

	grafica.yaxis.set_major_locator(MultipleLocator(1))
	grafica.yaxis.set_minor_locator(MultipleLocator(0.5))

	# Estableciendo formato

	grafica.yaxis.set_minor_formatter("{x:.1f} puntos")

	# Tamaño de (x, y)

	grafica.tick_params(axis = "y", which = "major", labelsize = 14)
	grafica.tick_params(axis = "x", which = "major", 
		labelsize = 14, labelrotation = 15)

# Limites Escalares

grafica.plot(x, y)
grafica.set_yscale("log")
grafica.set_ylim(0, 100000)

# Divisiones

grafica.set_xticks(np.arange(0, 20, 4), 
	["Android", "SQL", "Linux", "Window", "Mac"])

diagrama_de_barras()

plt.show()