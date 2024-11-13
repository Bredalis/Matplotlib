
import matplotlib.pyplot as plt
import numpy as np

def diagrama_de_puntos():
    fig, grafica = plt.subplots(subplot_kw = dict(projection = "polar"))

    # Datos
    matriz = np.linspace(0, 2, 20)
    colores = np.pi * matriz

    # Gráfico de dispersión polar
    visualizacion = grafica.scatter(colores, matriz, c = colores, s = 100, cmap = "hsv")
    plt.colorbar(mappable = visualizacion, location = "left")

diagrama_de_puntos()

# Datos para la matriz de colores
matriz  =  np.arange(36).reshape(6, 6)

# Mostrar una gráfica de colores a partir de la matriz
plt.imshow(
    matriz, cmap = "winter", interpolation = "bilinear",
    extent = [1, 10, 1, 10]
)
plt.show()