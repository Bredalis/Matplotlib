
# Librerias

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

# Datos para graficar

años = [
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020
]

nivel_1 = np.random.rand(10) * 100
nivel_2 = np.random.rand(10) * 200 + 100
nivel_3 = np.random.rand(10) * 300 + 200
nivel_4 = np.random.rand(10) * 400 + 300
nivel_5 = np.random.rand(10) * 500 + 400

# Grafica lineal

plt.plot(años, nivel_1, label = "Nivel 1", 
    color = "purple", marker = "<", linestyle = "-")

plt.plot(años, nivel_2, label = "Nivel 2", 
    color = "pink", marker = ">", linestyle = "--")

plt.plot(años, nivel_3, label = "Nivel 3", 
    color = "blue", marker = "*", linestyle = ":")

plt.plot(años, nivel_4, label = "Nivel 4", 
    color = "brown", marker = ".", linestyle = "-.")

plt.plot(años, nivel_5, label = "Nivel 5", 
    color = "black", marker = "+", linestyle = " ")

plt.legend()
plt.title("Examen de Certificacion")
plt.xlabel("años que se ha realizado el examen")
plt.ylabel("Puntaje")
plt.yticks(np.arange(0, 1001, 50))
plt.grid()
plt.minorticks_on()
plt.show()

# Barra vertical

x = np.arange(0, 10)

plt.bar(x, nivel_5, label = "Nivel 1", width = 1/5)
plt.bar(x + 0.2, nivel_4, label = "Nivel 2", width = 1/5)
plt.bar(x + 0.4, nivel_3, label = "Nivel 3", width = 1/5)
plt.bar(x + 0.6, nivel_2, label = "Nivel 4", width = 1/5)
plt.bar(x + 0.8, nivel_1, label = "Nivel 5", width = 1/5)
plt.show()

# Barra horizontal

plt.barh(x, nivel_5, label = "Nivel 1", height = 1/5)
plt.barh(x + 0.2, nivel_4, label = "Nivel 2", height = 1/5)
plt.barh(x + 0.4, nivel_3, label = "Nivel 3", height = 1/5)
plt.barh(x + 0.6, nivel_2, label = "Nivel 4", height = 1/5)
plt.barh(x + 0.8, nivel_1, label = "Nivel 5", height = 1/5)
plt.show()

# Barra aplicada

plt.bar(x, nivel_5, label = "Nivel 1", 
    bottom = nivel_2 + nivel_3 + nivel_4 + nivel_5)

plt.bar(x, nivel_4, label = "Nivel 2", bottom = nivel_3 + nivel_4 + nivel_5)
plt.bar(x, nivel_3, label = "Nivel 3", bottom = nivel_4 + nivel_5)
plt.bar(x, nivel_2, label = "Nivel 4", bottom = nivel_5)
plt.bar(x, nivel_1, label = "Nivel 5")
plt.show()

# Barra de dispercion

plt.scatter(x, nivel_5, label = "Nivel 1")
plt.scatter(x, nivel_4, label = "Nivel 2")
plt.scatter(x, nivel_3, label = "Nivel 3")
plt.scatter(x, nivel_2, label = "Nivel 4")
plt.scatter(x, nivel_1, label = "Nivel 5")
plt.show()

# Barra de pastel

plt.pie(nivel_1, 
    labels = ["Cereza", "Naranja", "Uva", "Fresa", "Pera", "Limon", 
    "Banana", "Tamarindo", "Coco", "Piña"])

plt.show()