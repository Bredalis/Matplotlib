
import matplotlib.pyplot as plt

# Lineas

plt.plot([1, 2, 3, 4], [1, 2, 3, 4], label = "Linea Azul")
plt.plot([1, 2, 3, 4], [1, 4, 3, 2], label = "Linea Naranja")

# Puntos

plt.scatter([1, 2, 3, 4], [4, 3, 2, 1], label = "Puntos")

plt.text(
	x = 2.5, y = 2.5, s = "Ubicacion de Texto",
	fontsize = 10, color = "green",

	bbox = dict(
		facecolor = "pink", edgecolor = "#003430",
		alpha = 0.8, boxstyle = "larrow"
))

# Cubos de mensajes

plt.annotate(
	"Nuevo Texto", (1.3, 2), xytext = (2, 1),
	arrowprops = dict(arrowstyle = "simple", 
	facecolor = "yellow", edgecolor = "k"))

plt.legend(loc = "upper center", shadow = 0, 
	fontsize = "x-large", facecolor = "pink")
plt.show()