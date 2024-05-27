
# Librerias

import matplotlib.pyplot as plt
import pandas as pd

# Obtener datos

personas = pd.read_csv("Personas.csv")
print(personas)

def grafica_circular(x, y):

	plt.scatter(personas[x], personas[y])

	x = x.capitalize()
	y = y.capitalize()

	plt.xlabel(x)
	plt.ylabel(y)
	plt.title(f"{x} y {y}")
	plt.show()

grafica_circular("altura", "peso")
grafica_circular("ingreso", "horas_trabajadas")
grafica_circular("ingreso", "ausencias")

# Matriz de correlacion

matriz = personas.corr()

plt.matshow(matriz, cmap = "bwr", vmin = -1, vmax = 1)
plt.xticks(range(5), personas.columns, rotation = 90)
plt.yticks(range(5), personas.columns)

# Matriz evaluativa

for i in range(len(matriz.columns)):
	for x in range(len(matriz.columns)):
		plt.text(i, x, round(matriz.iloc[0, 1], 2), 
			ha = "center", va = "center")

plt.colorbar()
plt.show()