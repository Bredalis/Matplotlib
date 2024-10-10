
# Librerías

import matplotlib.pyplot as plt
import numpy as np

# Grafica normal

eje_x = ["A", "B", "C", "D", "E"]
eje_y_1 = [10, 20, 30, 40, 50]
eje_y_2 = [20, 30, 40, 50, 60]

# Lineas

plt.plot(eje_x, eje_y_1)
plt.plot(eje_x, eje_y_2)
plt.show()

# Datos

años = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020
]

nivel_1 = np.random.rand(10) * 100
nivel_2 = np.random.rand(10) * 200 + 100
nivel_3 = np.random.rand(10) * 300 + 200
nivel_4 = np.random.rand(10) * 400 + 300
nivel_5 = np.random.rand(10) * 500 + 400

niveles = [nivel_1, nivel_2, nivel_3, nivel_4, nivel_5]
colores = ["purple", "pink", "blue", "brown", "black"]
marcadores = ["<", ">", "*", ".", "+"]
estilos = ["-", "--", ":", "-.", " "]

# Lineal

for i in range(1, 6):
    plt.plot(años, niveles[i - 1], label = f"Nivel {i}", 
    color = colores[i - 1], marker = marcadores[i - 1], linestyle = estilos[i - 1])

plt.legend()
plt.title("Examen de Certificacion")
plt.xlabel("años que se ha realizado el examen")
plt.ylabel("Puntaje")
plt.yticks(np.arange(0, 1001, 50))
plt.grid()
plt.minorticks_on()
plt.show()

# Vertical

x = np.arange(0, 10)
numeros = [0.0, 0.2, 0.4, 0.6, 0.8]

for i in range(1, 6):
    plt.bar(x + numeros[i - 1], niveles[i - 1], label = f"Nivel {i}", width = 1 / 5)    
plt.show()

# Horizontal

for i in range(1, 6):
    plt.barh(x + numeros[i - 1], niveles[i - 1], label = f"Nivel {i}", height = 1 / 5)    
plt.show()

# Aplicada

plt.bar(x, nivel_5, label = "Nivel 1", 
    bottom = nivel_2 + nivel_3 + nivel_4 + nivel_5)

plt.bar(x, nivel_4, label = "Nivel 2", bottom = nivel_3 + nivel_4 + nivel_5)
plt.bar(x, nivel_3, label = "Nivel 3", bottom = nivel_4 + nivel_5)
plt.bar(x, nivel_2, label = "Nivel 4", bottom = nivel_5)
plt.bar(x, nivel_1, label = "Nivel 5")
plt.show()

# Dispercion

for i in range(1, 6):
    plt.scatter(x, niveles[i - 1], label = f"Nivel {i}")
plt.show()

# Pastel

plt.pie(nivel_1, 
    labels = ["Cereza", "Naranja", "Uva", "Fresa", "Pera", "Limon", 
    "Banana", "Tamarindo", "Coco", "Piña"])

plt.show()