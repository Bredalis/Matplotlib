
# Librerias

import matplotlib.pyplot as plt
import numpy as np

# Dato para graficar

x = np.linspace(0, 2, 100)

# Tamaño de la grafica

plt.figure(figsize = (5, 3), layout = "constrained")

# Lineas

plt.plot(x, x, label = "Linea Azul")
plt.plot(x, x ** 2, label = "Linea Naranja")
plt.plot(x, x ** 3, label = "Linea Verde")

plt.title("Tema")
plt.xlabel("Etiqueta x")
plt.ylabel("Etiqueta Y")
plt.legend()
plt.show()