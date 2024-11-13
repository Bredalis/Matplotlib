
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd
import numpy as np

def diagrama_de_barras():
    fig, grafica = plt.subplots()

    # Datos del diagrama de barras
    df  =  pd.DataFrame({
        "Campos": ["Inglés", "Matemática", "Historia", "Lengua", "Física", "Biología"],
        "Cantidades": [6, 5, 4, 7, 5, 6]
    })

    grafica.bar(df["Campos"], df["Cantidades"], color = "skyblue")
    grafica.grid(axis = "y")

    # Etiquetas mayores y menores en el eje y
    grafica.set_yticks(range(0, 11, 2))
    grafica.set_yticks(np.arange(0, 10.5, 0.5), minor = True)

    # Limites del eje y
    grafica.set_ylim(0, 10)

    # Ubicación y formato de las divisiones en el eje y
    grafica.yaxis.set_major_locator(MultipleLocator(2))
    grafica.yaxis.set_minor_locator(MultipleLocator(0.5))
    grafica.yaxis.set_minor_formatter("{x:.1f} puntos")

    # Configuración del tamaño de etiquetas y rotación en los ejes
    grafica.tick_params(axis = "y", which = "major", labelsize = 14)
    grafica.tick_params(axis = "x", which = "major", labelsize = 14, rotation = 15)

# Crear gráfico de línea y configurar escala logarítmica
fig, grafica  =  plt.subplots()

# Datos del gráfico de línea
x  =  np.linspace(0, 20, 200)
y  =  x ** 3

grafica.plot(x, y, label = "x^3")

# Escala y límites del eje y
grafica.set_yscale("log")
grafica.set_ylim(0, 100000)

# Etiquetas personalizadas en el eje x
grafica.set_xticks(np.arange(0, 20, 4))
grafica.set_xticklabels(["Android", "SQL", "Linux", "Windows", "Mac"])

diagrama_de_barras()
plt.show()