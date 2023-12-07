
# Librerias

import numpy as np
import pandas as pd
import seaborn as sns
from math import sqrt
import scipy.stats as stats
import matplotlib.pyplot as plt

# Obtener datos

altura = pd.read_csv("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Datasets/CSV/personas.csv")
altura = altura["altura"]

print("\n Intervalo de confianza con un nivel de 95% \n")
print(stats.norm.interval(
	alpha = 0.95, loc = np.mean(altura), scale = altura.std(ddof = 1) / sqrt(altura.size)
))

print((altura.mean() - 1.960 * (altura.std(ddof = 1 / sqrt(altura.size)))), 
	altura.mean() - 1.960 * (altura.std(ddof = 1 / sqrt(altura.size))))

print("\n Calculo de valores z para un cierto nivel de confianza \n")
print("90%:", stats.norm.ppf(1 - (1 - 0.90) / 2))
print("95%:", stats.norm.ppf(1 - (1 - 0.95) / 2))
print("99%:", stats.norm.ppf(1 - (1 - 0.99) / 2))

# Grafica

df_alturas = pd.DataFrame()

df_alturas["Hombres"] = np.round(np.random.normal(170, 10, 100), 1)
df_alturas["Mujeres"] = np.round(np.random.normal(150, 10, 100), 1)

grafica = sns.barplot(data = df_alturas, ci = 99, capsize = 0.20)
grafica.set(title = "Intervalo de Confianza del 99%", ylabel = "altura Promedio (cm)")

plt.show()