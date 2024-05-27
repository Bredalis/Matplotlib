
import matplotlib.pyplot as plt

# Datos

x = range(12)
x_2 = range(13)

y = [20340, 21033, 21440, 22509, 23887, 21490, 
			22400, 24943, 23098, 23450, 26900, 28034]

y_2 = [20340, 21033, 21440, 22509, 23887, 
			21490, 22400, 24943, 23098, 23450, 26900, 28034, 24890]

print(f"Estilos: {plt.style.available}")

# Estilo de la grafica

plt.style.use("seaborn-v0_8-bright")

# Lineas

plt.plot(x, y, color = "k", linestyle = "dotted",
	marker = "p", label = "Linea Negra")
plt.plot(x_2, y_2, color = "b", linestyle = "dotted",
	marker = "o", label = "Linea Azul")

plt.xticks(x)
plt.tick_params(axis = "both", width = 1, top = 1, right = 1)

plt.title("Tema")
plt.xlabel("Etqiueta x")
plt.ylabel("Etqiueta y")
plt.legend()
plt.show()