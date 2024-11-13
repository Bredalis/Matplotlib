
import matplotlib.pyplot as plt

# Datos para el histograma
datos = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creación del histograma
plt.hist(datos, color = "pink", edgecolor = "black", bins = 5)
plt.show()