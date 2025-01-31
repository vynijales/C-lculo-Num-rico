import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
g = 9.81  # Aceleração devido à gravidade (m/s²)
k = 0.01  # Coeficiente de resistência do ar
v0 = 50   # Velocidade inicial (m/s)
theta = np.deg2rad(45)  # Ângulo de lançamento (45 graus)

# Condições iniciais
x0 = 0  # Posição horizontal inicial
y0 = 0  # Posição vertical inicial
vx0 = v0 * np.cos(theta)  # Velocidade horizontal inicial
vy0 = v0 * np.sin(theta)  # Velocidade vertical inicial

# Função que define as equações diferenciais
def equations_of_motion(state, t):
    x, y, vx, vy = state
    dxdt = vx
    dydt = vy
    dvxdt = -k * vx**2
    dvydt = -g - k * vy**2
    return [dxdt, dydt, dvxdt, dvydt]

# Método de Runge-Kutta de 4ª ordem
def runge_kutta_4th_order(f, state, t, dt):
    k1 = f(state, t)
    k2 = f([s + 0.5 * dt * k for s, k in zip(state, k1)], t + 0.5 * dt)
    k3 = f([s + 0.5 * dt * k for s, k in zip(state, k2)], t + 0.5 * dt)
    k4 = f([s + dt * k for s, k in zip(state, k3)], t + dt)
    return [s + (dt / 6) * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) for i, s in enumerate(state)]

# Simulação
t0 = 0  # Tempo inicial
tf = 10  # Tempo final
dt = 0.01  # Passo de tempo

# Inicialização
t_values = np.arange(t0, tf, dt)
state = [x0, y0, vx0, vy0]  # Estado inicial [x, y, vx, vy]
x_values, y_values = [], []

# Loop de simulação
for t in t_values:
    x_values.append(state[0])
    y_values.append(state[1])
    state = runge_kutta_4th_order(equations_of_motion, state, t, dt)

    # Parar se o projétil atingir o solo (y < 0)
    if state[1] < 0:
        break

# Plotar a trajetória
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label="Trajetória do Projétil")
plt.xlabel("Posição Horizontal (m)")
plt.ylabel("Posição Vertical (m)")
plt.title("Simulação do Movimento de um Projétil com Resistência do Ar")
plt.grid()
plt.legend()
plt.show()