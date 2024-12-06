import math

def f(x):
    return (math.e ** (39.0744 * x)) * (1 + 39.0744 * x) - (math.e ** 19.5372)

def derivada(x, eps):
    return (f(x + eps) - f(x)) / eps

def newton(x0, eps, max_iter):
    x = x0
    it = 0

    while abs(f(x)) > eps and it < max_iter:
        df = derivada(x, eps)
        if df == 0:
            raise ValueError("Método falhou (Divisão por 0)")
        
        x = x - f(x) / df
        it += 1

    return x, it


eps = 10e-5
raiz, it = newton(1, eps, 10000)
print(f"Valor encontrado com o método de Newton: {raiz} em {it} iterações")
