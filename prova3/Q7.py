import numpy as np
import matplotlib.pyplot as plt

g = 9.81
r = 6.37e6

x = 0 # Tempo inicial
y = 0 # Posicão inicial
v = 1400 # Velocidade inicial

max_iteracoes = 100000

pontos_x = []
pontos_y = []

h = 1

for i in range(max_iteracoes):
    pontos_x.append(x)
    pontos_y.append(y)
    
    aceleracao = g * (r ** 2) / ((r + y) ** 2)
    v = v - aceleracao * h
    y = y + v * h

    x += h

    # Para quando o projétil voltar a altura 0
    if y <= 0:
        break


x_max = np.argmax(pontos_y)
y_max = pontos_y[x_max]

plt.title("Trajetória do Projétil")
plt.xlabel("Tempo (s)")
plt.ylabel("Altura (m)")

plt.plot(pontos_x, pontos_y)
plt.plot(x_max, y_max, markersize=5, marker='o')
plt.annotate(f"Altura Máxima: {y_max:.2f}m", xy=(x_max, y_max), xytext=(x_max + 30, y_max + 100), arrowprops=dict(arrowstyle = '-', connectionstyle = 'arc3', facecolor='red'))
plt.show()