''''
3ª Questão: Implemente o método da bissecção usando a linguagem de
programação Python. O algoritmo deve fornecer como resposta se uma
função escolhida pelo usuário possui ou não raiz em um intervalo [a, b]
escolhido também pelo usuário. Cuide para que seu algoritmo analise todas
as possibilidades acerca da escolha da raiz. A quantidade de interações do
algoritmo não pode ser superior a

Onde a e b são os extremos do intervalo e 𝜀 a precisão do problema. Meça
também o tempo de execução e a quantidade de iterações necessárias para
encontrar a raiz.
'''
import math

def f(x):
    return x * x + x - 6.0

# Precisão
eps = 0.001

def bis(a, b, k=None, iterations=0):
    if k is None:
        # Calcula o número máximo de iterações teórico para a precisão dada
        k = math.ceil((math.log(b - a) - math.log(eps)) / math.log(2))
    
    c = (a + b) / 2  # Ponto médio do intervalo
    
    # Verificações de parada (raízes nos extremos)
    if abs(f(a)) < eps:
        return a, iterations + 1
    elif abs(f(b)) < eps:
        return b, iterations + 1

    # Verifica se o número de iterações foi excedido
    if k < 0:
        return None, iterations + 1

    if abs(f(c)) < eps:
        return c, iterations + 1

    # Recursão nos subintervalos (Caso haja raízes nos subintervalos)
    if f(a) * f(c) < 0:
        return bis(a, c, k - 1, iterations + 1)
    elif f(c) * f(b) < 0:
        return bis(c, b, k - 1, iterations + 1)
    
    # Recursão nos subintervalos (Caso não haja raízes nos subintervalos)
    r1 = bis(a, c, k-1)
    r2 = bis(c, b, k-1)
    
    if r1 is None:
        return r2
    elif r2 is None:
        return r1
    # Caso haja mais de uma raiz nos subintervalos, retorna a raiz mais próxima de 0
    else:
        return min(abs(f(r1)), abs(f(r2)))


# Testando a função
raiz, total_iteracoes = bis(0, 3)

# Imprimindo a raiz e o total de iterações
print(f"Raiz encontrada pelo método da bissecção: {raiz} em {total_iteracoes} iterações")