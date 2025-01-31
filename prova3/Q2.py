import numpy as np
import math

def simpson_1_3_composto(func, a, b, n):
    # Verificar se o número de subintervalos é par
    if n % 2 != 0:
        raise ValueError("O número de subintervalos (n) deve ser par.")
    
    # Passo (largura de cada subintervalo)
    h = (b - a) / n
    
    # Pontos de avaliação
    x = np.linspace(a, b, n + 1)
    
    # Cálculo da soma ponderada
    integral = func(x[0]) + func(x[-1])  # Termos nos extremos
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * func(x[i])  # Termos com peso 2
        else:
            integral += 4 * func(x[i])  # Termos com peso 4
    
    # Multiplicar pelo fator (h/3)
    integral *= (h / 3)
    
    return integral

def simpson_3_8(func, a, b, n):
    # Verifica se o número de subintervalos é múltiplo de 3
    if n % 3 != 0:
        raise ValueError("O número de subintervalos (n) deve ser múltiplo de 3.")
    
    # Passo (largura de cada subintervalo)
    h = (b - a) / n
    
    # Pontos de avaliação (array contendo os n+1 pontos igualmente espaçados no intervalo [a, b])
    x = np.linspace(a, b, n + 1)
    
    # Cálculo da soma ponderada
    integral = func(x[0]) + func(x[-1])  # Termos nos extremos
    for i in range(1, n):
        if i % 3 == 0:
            integral += 2 * func(x[i]) # Termos múltiplos de 3
        else:
            integral += 3 * func(x[i]) # Outros termos
    
    # Multiplicar pelo fator (3h/8)
    integral *= (3 * h / 8)
    
    return integral

if __name__ == "__main__":
    # Define a função a ser integrada
    def f(x):
        return math.sqrt(1 - x**2)
    
    
    # Limites da integral e número de subintervalos
    a = -1
    b = 1
    n_8 = 8
    n_9 = 9
    
    # Calcula a integral
    resultado_1_3 = simpson_1_3_composto(f, a, b, n_8)
    resultado_3_8 = simpson_3_8(f, a, b, n_9)
    print(f"Aproximação da integral por Simpson 1/3 em 8 subintervalos: {resultado_1_3}")
    print(f"Aproximação da integral por Simpson 3/8 em 9 subintervalos: {resultado_3_8}")
