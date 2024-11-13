
import matplotlib.pyplot as plt
import numpy as np

# Configuración de la gráfica
fig, grafica = plt.subplots()

# Datos
x = np.linspace(0.1, 6)
y = np.sin(x)

# Línea de tallo (stem plot)
grafica.stem(x, y, linefmt = "k:", markerfmt = "D", basefmt = "C3--")

# Configuración de los ejes
grafica.spines["left"].set_color("blue")
grafica.spines["right"].set_color("red")
grafica.spines["left"].set_linewidth(1)
grafica.spines["right"].set_linewidth(1)
grafica.spines["left"].set_alpha(0.5)
grafica.spines["right"].set_alpha(0.5)
grafica.spines["left"].set_linestyle("dashed")
grafica.spines["right"].set_linestyle("dashed")
grafica.spines["left"].set_visible(True)
grafica.spines["right"].set_visible(True)

# Línea de fondo
grafica.grid(True, linewidth = 1)
plt.show()