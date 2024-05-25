
import matplotlib.pyplot as plt

# Datos para graficar

datos = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Histograma

plt.hist(datos, color = "pink", ec = "black", bins = 5)
plt.show()