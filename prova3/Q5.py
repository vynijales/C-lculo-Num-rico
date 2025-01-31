import numpy as np
import matplotlib.pyplot as plt

# Definição do modelo SIR
def sir_model(y, beta, gamma):
    S, I, R = y
    dS_dt = -beta * S * I
    dI_dt = beta * S * I - gamma * I
    dR_dt = gamma * I
    return np.array([dS_dt, dI_dt, dR_dt])

# Método de Runge-Kutta de quarta ordem (RK4) para resolver EDOs
def runge_kutta(f, y0, t, beta, gamma):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    
    for i in range(n - 1):
        dt = t[i+1] - t[i]
        k1 = dt * f(y[i], beta, gamma)
        k2 = dt * f(y[i] + 0.5 * k1, beta, gamma)
        k3 = dt * f(y[i] + 0.5 * k2, beta, gamma)
        k4 = dt * f(y[i] + k3, beta, gamma)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return y

# Parâmetros do modelo
beta = 0.3  # Taxa de transmissão
gamma = 0.1  # Taxa de recuperação

# Condições iniciais
populacao_total = 1000
S0 = 990 / populacao_total  # 990 pessoas suscetíveis
I0 = 10 / populacao_total   # 10 pessoas infectadas
R0 = 0 / populacao_total    # Ninguém recuperado inicialmente

# Tempo de simulação
tempo_simulacao = np.linspace(0, 160, 1000)  # 160 dias

# Resolver o sistema usando Runge-Kutta
solucao = runge_kutta(sir_model, [S0, I0, R0], tempo_simulacao, beta, gamma)

# Plotar os resultados
plt.figure(figsize=(10, 6))
plt.plot(tempo_simulacao, solucao[:, 0], label="Suscetíveis", color='blue')
plt.plot(tempo_simulacao, solucao[:, 1], label="Infectados", color='red')
plt.plot(tempo_simulacao, solucao[:, 2], label="Recuperados", color='green')
plt.xlabel("Tempo (dias)")
plt.ylabel("Proporção da População")
plt.legend()
plt.title("Modelo SIR - Propagação de Doença Infecciosa")
plt.grid()
plt.show()