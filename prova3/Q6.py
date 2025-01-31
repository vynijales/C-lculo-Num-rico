import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_4th_order(f, y0, t0, h, t_max):
    t_values = [t0]
    y_values = [y0]
    
    t = t0
    y = y0
    
    while t <= t_max:
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        t = t + h
        
        t_values.append(t)
        y_values.append(y)
    
    return np.array(t_values), np.array(y_values)

def euler_method(f, y0, t0, h, t_max):
    t_values = [t0]
    y_values = [y0]
    
    t = t0
    y = y0
    
    while t <= t_max:
        y = y + h * f(t, y)
        t = t + h
        
        t_values.append(t)
        y_values.append(y)
    
    return np.array(t_values), np.array(y_values)

def dvdt(t, v):
    g = 9.81  # aceleração da gravidade (m/s²)
    c = 0.225  # coeficiente de arrasto (kg/m)
    m = 90  # massa (kg)
    return g - (c/m) * v**2

def calcular_movimento():
    h = 0.1  # passo de integração
    v0 = 0  # velocidade inicial (m/s)
    altura_inicial = 1000  # altura inicial (m)
    
    # Resolver para velocidade usando Runge-Kutta
    t_rk, v_rk = runge_kutta_4th_order(dvdt, v0, 0, h, 200)
    
    # Resolver para velocidade usando Euler
    t_euler, v_euler = euler_method(dvdt, v0, 0, h, 200)
    
    # Resolver para posição integrando numericamente a velocidade
    s_rk = [altura_inicial]
    s_euler = [altura_inicial]
    
    tempo_queda_rk = None
    velocidade_final_rk = None
    tempo_queda_euler = None
    velocidade_final_euler = None
    
    for i in range(1, len(v_rk)):
        nova_altura = s_rk[-1] - v_rk[i-1] * h
        if nova_altura <= 0:
            tempo_queda_rk = t_rk[i]
            velocidade_final_rk = v_rk[i]
            break
        s_rk.append(nova_altura)
    
    for i in range(1, len(v_euler)):
        nova_altura = s_euler[-1] - v_euler[i-1] * h
        if nova_altura <= 0:
            tempo_queda_euler = t_euler[i]
            velocidade_final_euler = v_euler[i]
            break
        s_euler.append(nova_altura)
    
    print(f"Método de Runge-Kutta: Tempo até a queda = {tempo_queda_rk:.2f} s, Velocidade final = {velocidade_final_rk:.2f} m/s")
    print(f"Método de Euler: Tempo até a queda = {tempo_queda_euler:.2f} s, Velocidade final = {velocidade_final_euler:.2f} m/s")
    
    # Ajustar o tempo para os gráficos
    tempo_limite = max(tempo_queda_rk, tempo_queda_euler) + 3
    
    # Plotar os resultados
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t_rk[:len(s_rk)], v_rk[:len(s_rk)], label='Velocidade RK4 (m/s)')
    plt.plot(t_euler[:len(s_euler)], v_euler[:len(s_euler)], label='Velocidade Euler (m/s)', linestyle='dashed')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s)')
    plt.xlim(0, tempo_limite)
    plt.legend()
    plt.grid()
    
    plt.subplot(1, 2, 2)
    plt.plot(t_rk[:len(s_rk)], s_rk, label='Altura RK4 (m)', color='r')
    plt.plot(t_euler[:len(s_euler)], s_euler, label='Altura Euler (m)', color='b', linestyle='dashed')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Altura (m)')
    plt.legend()
    plt.grid()
    
    plt.show()

calcular_movimento()