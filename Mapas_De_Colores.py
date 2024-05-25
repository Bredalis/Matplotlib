
# Librerias

import matplotlib.pyplot as plt
import pandas as pd

# Obtener datos

personas = pd.read_csv("Personas.csv")
print(personas)

# Graficas circulares

plt.scatter(personas["altura"], personas["peso"])
plt.xlabel("Altura (cms)")
plt.ylabel("Peso (kgs)")
plt.title("Altura y Peso")
plt.show()

plt.scatter(personas["ingreso"], personas["horas_trabajadas"])
plt.xlabel("Ingreso ($)")
plt.ylabel("Horas Trabajadas")
plt.title("Ingreso y Horas")
plt.show()

plt.scatter(personas["ingreso"], personas["ausencias"])
plt.xlabel("Ingreso ($)")
plt.ylabel("Ausencias")
plt.title("Ingresos y Ausencias")
plt.show()

# Matriz de correlacion

matriz = personas.corr()

plt.matshow(matriz, cmap = "bwr", vmin = -1, vmax = 1)
plt.xticks(range(5), personas.columns, rotation = 90)
plt.yticks(range(5), personas.columns)

# Matriz evaluativa

for i in range(len(matriz.columns)):
	for x in range(len(matriz.columns)):
		plt.text(i, x, round(matriz.iloc[0, 1], 2), 
			ha = "center", va = "center")

plt.colorbar()
plt.show()