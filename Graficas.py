
import matplotlib.pyplot as plt
import numpy as np

# Datos para la gráfica de dispersión y la línea
x = np.arange(8)
y = [3, 1, 1, 2, 5, 5, 7, 6]

def diagrama_de_barras():
    fig, grafica = plt.subplots()

    # Datos del diagrama de barras
    sentimientos = ["Alegría", "Enojo", "Tristeza", "Miedo", "Desagrado"]
    cantidad = [16, 5, 7, 10, 14]

    grafica.bar(sentimientos, cantidad, color = "aqua")
    grafica.set_title("Sustantivos Abstractos")

# Crear figura y gráfica para dispersión y línea
fig, grafica = plt.subplots()

# Gráfico de dispersión (círculos)
grafica.scatter(x, y, s = 200, color = "#ff0345", edgecolor = "k", label = "Puntos")

# Gráfico de línea
grafica.plot(x, y, color = "blue", linewidth = 5, zorder = 0, label = "Línea")
grafica.set_title("Gráfico de Dispersión y Línea")
grafica.legend()

# Crear una segunda figura y gráfica sencilla
fig, grafica2 = plt.subplots()
grafica2.plot([1, 2, 3, 4], [1, 2, 4, 3], color = "purple", marker = "o")
grafica2.set_title("Primera Gráfica Simple")

diagrama_de_barras()
plt.show()