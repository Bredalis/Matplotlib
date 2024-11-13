
import matplotlib.pyplot as plt

# Líneas
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], label = "Línea Azul")
plt.plot([1, 2, 3, 4], [1, 4, 3, 2], label = "Línea Naranja")

# Puntos
plt.scatter([1, 2, 3, 4], [4, 3, 2, 1], label = "Puntos")

# Texto en ubicación específica
plt.text(
    x = 2.5, y = 2.5, s = "Ubicación de Texto",
    fontsize = 10, color = "green",
    bbox = dict(
        facecolor = "pink", edgecolor = "#003430",
        alpha = 0.8, boxstyle = "larrow"
    )
)

# Anotación con flecha
plt.annotate(
    "Nuevo Texto", xy = (1.3, 2), xytext = (2, 1),
    arrowprops = dict(arrowstyle = "simple", 
    	facecolor = "yellow", edgecolor = "k")
)

# Leyenda
plt.legend(loc = "upper center", shadow = False, 
           fontsize = "x-large", facecolor = "pink")
plt.show()