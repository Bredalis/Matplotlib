
# Librerías

import matplotlib.pyplot as plt
import numpy as np

# Datos

x = np.arange(8)
y = [3, 1, 1, 2, 5, 5, 7, 6]

def diagrama_de_barras():

	# Grafica

	fig, grafica = plt.subplots()

	sentimietos = ["Alegria", "Enojo", "Tristeza", "Miedo", "Desagrado"]
	cantidad = [16, 5, 7, 10, 14]

	# Barra

	plt.title("Sustantivos Abstractos")
	grafica.bar(sentimietos, cantidad, color = "aqua")

# Circulos

plt.scatter(x, y, s = 200, color = "#ff0345", edgecolor = ("k"))

# Lineas

plt.plot(x, y, c = "b", linewidth = 5, zorder = 0)

# Grafica 2

fig, grafica = plt.subplots()

grafica.plot([1, 2, 3, 4], [1, 2, 4, 3])
plt.title("Primera Grafica")

diagrama_de_barras()

plt.show()