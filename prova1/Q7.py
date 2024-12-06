''''
7ªQuestão Implemente usando a linguagem Python os métodos de Newton
e da secante. Compare os métodos, análise qual executa menos iterações e
menos tempo para o cálculo da raiz de uma função escolhida pelo usuário.
'''
from time import perf_counter as time

def f(x):
    return x ** 3 - 9 * x + 3

def derivada(x, eps):
    return (f(x + eps) - f(x)) / eps

def newton(x0, eps, max_iter):
    x = x0
    it = 0

    while abs(f(x)) > eps and it < max_iter:
        df = derivada(x, eps)
        if df == 0:
            raise ValueError("A derivada é 0, ocorrerá uma divisão por 0")
        
        x = x - f(x) / df
        it += 1

    return x, it


def secante(x0, x1, eps, max_iter):
    it = 0
    while abs(f(x1)) > eps and it < max_iter:
        if (f(x1) == f(x0)):
            raise ValueError("Método falhou")
        x_novo = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x_novo
        it += 1

    return x1, it

eps = 0.0001
x0 = float(input("x0: "))
x1 = float(input("x1 (para o método da secante): "))

t0 = time()
raiz_newton, it_newton = newton(x0, eps, 100)
t1 = time()
tempo_newton = (t1 - t0) * 1000

t0 = time()
raiz_secante, it_secante = secante(x0, x1, eps, 100)
t1 = time()
tempo_secante = (t1 - t0) * 1000

print(f"Raíz aproximada pelo método de Newton: {raiz_newton} em {it_newton} iterações. Tempo: {tempo_newton}ms")
print(f"Raíz aproximada pelo método da secante: {raiz_secante} em {it_secante} iterações. Tempo: {tempo_secante}ms")
