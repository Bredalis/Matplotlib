
import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 2, 100)

# Tamaño de la gráfica y configuración
plt.figure(figsize = (5, 3), layout = "constrained")

# Gráficas de líneas
plt.plot(x, x, label = "Línea Azul")
plt.plot(x, x ** 2, label = "Línea Naranja")
plt.plot(x, x ** 3, label = "Línea Verde")

# Títulos y etiquetas
plt.title("Tema")
plt.xlabel("Etiqueta x")
plt.ylabel("Etiqueta y")
plt.legend()

plt.show()