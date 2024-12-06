''''
6ªQuestão Implemente usando a linguagem Python o método do ponto fixo,
meça a quantidade de iterações e o tempo de execução deste método.
Atenção no momento de escolher a função de iteração 𝜑. Escolha uma
função, um intervalo e uma precisão e compare quantidade de iterações entre
o método do ponto fixo e os métodos da bissecção.
'''
from time import perf_counter as time
from Q3_bisseccao import bis

def f(x):
    return x * x + x - 6.0

def g(x):
    return 6.0 / (x + 1.0)

def pf(a, eps):
    it = 0
    c = a # Ponto inicial
    gc = g(c)
    while abs(f(gc)) > eps:
        it += 1
        c = gc
        gc = g(c)

    return gc, it

a = float(input("A: "))
b = float(input("B: "))

if f(a) * f(b) > 0:
    print("Não foi possível calcular o valor nesse intervalo")


print("***Método do Ponto Fixo***")

eps = 0.0001
ti = time()
raiz, pf_iteracoes = pf(a, eps)
tf = time()

print(f"Raíz aproximada: {raiz} em {pf_iteracoes} iterações")
print(f"Tempo de execução: {(tf - ti) * 1000}ms\n")

# Metodo da bissecção
print("***Método da Bissecção***")

ti = time()
raiz_bis, total_iteracoes = bis(a, b)
tf = time()

print(f"Raiz encontrada: {raiz_bis} em {total_iteracoes} iterações")
print(f"Tempo de execução: {(tf - ti) * 1000}ms")