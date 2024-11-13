
import matplotlib.pyplot as plt

# Datos
x = range(12)
x_2 = range(13)
y = [20340, 21033, 21440, 22509, 23887, 21490, 22400, 24943, 23098, 23450, 26900, 28034]
y_2 = [20340, 21033, 21440, 22509, 23887, 21490, 22400, 24943, 23098, 23450, 26900, 28034, 24890]

# Estilos de gráfico disponibles
print(f"Estilos: {plt.style.available}")

# Aplicar estilo de gráfico
plt.style.use("seaborn-v0_8-bright")

# Gráficas de líneas
plt.plot(x, y, color = "k", linestyle = "dotted", marker = "p", label = "Línea Negra")
plt.plot(x_2, y_2, color = "b", linestyle = "dotted", marker = "o", label = "Línea Azul")

# Configuración de los ejes y etiquetas
plt.xticks(x)
plt.tick_params(axis = "both", width = 1, top = True, right = True)
plt.title("Tema")
plt.xlabel("Etiqueta x")
plt.ylabel("Etiqueta y")
plt.legend()
plt.show()