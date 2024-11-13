
import matplotlib.pyplot as plt
import pandas as pd

# Obtener datos
personas = pd.read_csv("Personas.csv")
print(personas)

def grafica_circular(x, y):
    """Función para graficar dispersión entre dos variables."""
    plt.scatter(personas[x], personas[y])

    # Configuración de etiquetas
    x_label = x.capitalize()
    y_label = y.capitalize()
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f"{x_label} y {y_label}")
    plt.show()

# Graficas de dispersión entre diferentes pares de datos
grafica_circular("altura", "peso")
grafica_circular("ingreso", "horas_trabajadas")
grafica_circular("ingreso", "ausencias")

# Matriz de correlación
matriz = personas.corr()

plt.matshow(matriz, cmap = "bwr", vmin = -1, vmax = 1)
plt.xticks(range(len(personas.columns)), personas.columns, rotation = 90)
plt.yticks(range(len(personas.columns)), personas.columns)

# Mostrar valores dentro de la matriz de correlación
for i in range(len(matriz.columns)):
    for j in range(len(matriz.columns)):
        plt.text(i, j, round(matriz.iloc[i, j], 2), 
        	ha = "center", va = "center")

plt.colorbar()
plt.show()