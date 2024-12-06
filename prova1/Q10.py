import math

# Dados fornecidos
L = 3  # Comprimento da viga (m)
E = 70 * 10**9  # Módulo de elasticidade (Pa)
I = 52.9 * 10**-6  # Momento de inércia (m^4)
w0 = 15 * 10**3  # Carga (N/m)
y_target = 0.009  # Deflexão desejada (m)

# Função y(x)
def y(x):
    term1 = (48 * L**3) * math.cos((math.pi / (2 * L)) * x)
    term2 = -48 * L**3
    term3 = 3 * (math.pi**3) * L * (x**2)
    term4 = -math.pi**3 * (x**3)
    return (w0 * L / (3 * (math.pi**4) * E * I)) * (term1 + term2 + term3 + term4)

# Função para o método de Newton e Secante (g(x) = y(x) - y_target)
def g(x):
    return y(x) - y_target

# Derivada numérica de g(x)
def derivada(x, epsilon=1e-6):
    return (g(x + epsilon) - g(x)) / epsilon

# Método de Newton
def metodo_newton(x0, epsilon, max_iter=100):
    x = x0
    iter_count = 0
    print("\nMétodo de Newton:")
    print("Iteração | x (m)           | y(x) (m)")
    print("--------------------------------------")

    while abs(g(x)) > epsilon and iter_count < max_iter:
        df = derivada(x)
        if df == 0:
            raise ValueError("A derivada é zero. O método de Newton pode falhar.")
        
        y_val = y(x)  # Valor de y(x)
        print(f"{iter_count + 1:>8} | {x:>15.6f} | {y_val:>15.6f}")

        x = x - g(x) / df
        iter_count += 1

    y_val = y(x)  # Valor final de y(x)
    print(f"{iter_count + 1:>8} | {x:>15.6f} | {y_val:>15.6f}")

    return x, iter_count

# Método da Secante
def metodo_secante(x0, x1, epsilon, max_iter=100):
    iter_count = 0
    print("\nMétodo da Secante:")
    print("Iteração | x (m)           | y(x) (m)")
    print("--------------------------------------")

    while abs(g(x1)) > epsilon and iter_count < max_iter:
        if g(x1) == g(x0):
            raise ValueError("Divisão por zero na iteração. Método falhou.")
        
        y_val = y(x1)  # Valor de y(x)
        print(f"{iter_count + 1:>8} | {x1:>15.6f} | {y_val:>15.6f}")

        x_new = x1 - g(x1) * (x1 - x0) / (g(x1) - g(x0))
        x0, x1 = x1, x_new
        iter_count += 1

    y_val = y(x1)  # Valor final de y(x)
    print(f"{iter_count + 1:>8} | {x1:>15.6f} | {y_val:>15.6f}")

    return x1, iter_count

# Entrada inicial
x0_newton = 1.0  # Chute inicial para o método de Newton
x0_secante = 0.5  # Primeiro chute inicial para o método da Secante
x1_secante = 2.0  # Segundo chute inicial para o método da Secante
epsilon = 1e-6  # Precisão

# Soluções
raiz_newton, iter_newton = metodo_newton(x0_newton, epsilon)
raiz_secante, iter_secante = metodo_secante(x0_secante, x1_secante, epsilon)

# Resultados finais
print("\nResultados finais:")
print(f"Método de Newton: raiz aproximada = {raiz_newton:.6f} m, iterações = {iter_newton}")
print(f"Método da Secante: raiz aproximada = {raiz_secante:.6f} m, iterações = {iter_secante}")
