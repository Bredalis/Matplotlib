
# Librerias

import matplotlib.pyplot as plt
import numpy as np

# Grafica

fig, grafica = plt.subplots()

# Datos para graficar

x = np.linspace(0.1, 6)
y = np.sin(x)

# Origen

grafica.stem(x, y, linefmt = "k:", markerfmt = "D", basefmt = "C3--")

# Colocaciones

grafica.spines["left"].set_color("blue")
grafica.spines["right"].set_color("red")

grafica.spines["left"].set_linewidth(1)
grafica.spines["right"].set_linewidth(1)

grafica.spines["left"].set_alpha(0.5)
grafica.spines["right"].set_alpha(0.5)

grafica.spines["left"].set_linestyle("dashed")
grafica.spines["right"].set_linestyle("dashed")

grafica.spines["left"].set_visible(1)
grafica.spines["right"].set_visible(1)

# Linea de fondo

grafica.grid(1, linewidth = 1)
plt.show()