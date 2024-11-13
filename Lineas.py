
import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 20, 10)
y  = x ** 2
x_2 = np.linspace(21, 30, 10)
y_2 = x_2 ** 2

# Dos líneas
plt.plot(x, y, "rd-", label = "Línea Roja")
plt.plot(x_2, y_2, "ko:", label = "Línea Negra")

# Líneas de fondo
plt.grid(axis = "y", color = "b", which = "major", alpha = 0.5, linestyle = "--")
plt.grid(axis = "x", color = "b", which = "major", alpha = 0.2, linestyle = "--")

# Tamaño de las etiquetas de los ejes y leyenda
plt.tick_params(axis = "y", which = "major", labelsize = 15)
plt.legend()
plt.show()