
import matplotlib.pyplot as plt
import numpy as np

# Gráfica de líneas simple
eje_x = ["A", "B", "C", "D", "E"]
eje_y_1 = [10, 20, 30, 40, 50]
eje_y_2 = [20, 30, 40, 50, 60]

plt.plot(eje_x, eje_y_1)
plt.plot(eje_x, eje_y_2)
plt.show()

# Datos para gráficos complejos
anios = list(range(2011, 2021))
nivel_1 = np.random.rand(10) * 100
nivel_2 = np.random.rand(10) * 200 + 100
nivel_3 = np.random.rand(10) * 300 + 200
nivel_4 = np.random.rand(10) * 400 + 300
nivel_5 = np.random.rand(10) * 500 + 400

niveles = [nivel_1, nivel_2, nivel_3, nivel_4, nivel_5]
colores = ["purple", "pink", "blue", "brown", "black"]
marcadores = ["<", ">", "*", ".", "+"]
estilos = ["-", "--", ":", "-.", " "]

# Gráfico de líneas con variación de estilos
for i in range(5):
    plt.plot(
        anios, niveles[i], label = f"Nivel {i + 1}", 
        color = colores[i], marker = marcadores[i], linestyle = estilos[i]
    )

plt.legend()
plt.title("Examen de Certificación")
plt.xlabel("Años")
plt.ylabel("Puntaje")
plt.yticks(np.arange(0, 1001, 50))
plt.grid()
plt.minorticks_on()
plt.show()

# Gráfico de barras verticales
x = np.arange(10)
offsets = [0.0, 0.2, 0.4, 0.6, 0.8]

for i in range(5):
    plt.bar(x + offsets[i], niveles[i], label = f"Nivel {i + 1}", width = 0.2)
plt.legend()
plt.show()

# Gráfico de barras horizontales
for i in range(5):
    plt.barh(x + offsets[i], niveles[i], label = f"Nivel {i + 1}", height = 0.2)
plt.legend()
plt.show()

# Gráfico de barras apiladas
plt.bar(x, nivel_5, label = "Nivel 1", bottom = nivel_2 + nivel_3 + nivel_4 + nivel_5)
plt.bar(x, nivel_4, label = "Nivel 2", bottom = nivel_3 + nivel_4 + nivel_5)
plt.bar(x, nivel_3, label = "Nivel 3", bottom = nivel_4 + nivel_5)
plt.bar(x, nivel_2, label = "Nivel 4", bottom = nivel_5)
plt.bar(x, nivel_1, label = "Nivel 5")
plt.legend()
plt.show()

# Gráfico de dispersión
for i in range(5):
    plt.scatter(x, niveles[i], label = f"Nivel {i + 1}")
plt.legend()
plt.show()

# Gráfico circular (pastel)
plt.pie(
    nivel_1, 
    labels = ["Cereza", "Naranja", "Uva", "Fresa", "Pera", "Limón", 
    "Banana", "Tamarindo", "Coco", "Piña"]
)
plt.show()