import math

def f(x):
    return x * x + x - 6.0

eps = 0.001

def bis(a, b, k=None, iterations=0):
    if k is None:
        # Calcula o número máximo de iterações teórico para a precisão dada
        k = math.ceil((math.log(b - a) - math.log(eps)) / math.log(2))
    
    c = (a + b) / 2  # Ponto médio do intervalo
    
    if abs(f(a)) < eps:
        return a, iterations + 1
    elif abs(f(b)) < eps:
        return b, iterations + 1

    if k < 0:
        return None, iterations + 1

    if abs(f(c)) < eps:
        return c, iterations + 1

    # Recursão nos subintervalos
    if f(a) * f(c) < 0:
        return bis(a, c, k - 1, iterations + 1)
    elif f(c) * f(b) < 0:
        return bis(c, b, k - 1, iterations + 1)

if __name__ == "__main__":
    # Testando a função
    raiz, total_iteracoes = bis(0, 3)

    # Imprimindo a raiz e o total de iterações
    print(f"Raiz encontrada pelo método da bissecção: {raiz} em {total_iteracoes} iterações")