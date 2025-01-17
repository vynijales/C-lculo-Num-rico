import numpy as np
import random
import math

def metodo_gauss_jacobi(M, c, x_inicial, epsilon, max_iteracoes=100000):
    n = len(c)
    x_atual = x_inicial.copy()
    x_proximo = np.zeros_like(x_atual)

    for iteracao in range(max_iteracoes):
        for i in range(n):
            soma = np.dot(M[i, :i], x_atual[:i]) + np.dot(M[i, i + 1:], x_atual[i + 1:])
            x_proximo[i] = (c[i] - soma) / M[i, i]

        if np.linalg.norm(x_proximo - x_atual, ord=np.inf) < epsilon:  # Critério de parada
            return x_proximo, iteracao + 1

        x_atual = x_proximo.copy()

    raise ValueError("O método de Gauss-Jacobi não convergiu no número máximo de iterações.")

def verificar_zero_diagonal(M):
    return any(M[i, i] == 0 for i in range(len(M)))

def verificar_vetor_constante(vetor):
    return all(valor == vetor[0] for valor in vetor)

def possui_diagonal_dominante(M):
    for i in range(len(M)):
        soma = sum(abs(M[i, j]) for j in range(len(M)) if i != j)
        if abs(M[i, i]) <= soma:
            return False
    return True

def validar_raizes(M, c, raizes, epsilon):
    for i in range(len(M)):
        resultado = sum(M[i, j] * raizes[j] for j in range(len(M)))
        print(f"Resultado da linha {i}: {resultado}")
        if not math.isclose(resultado, c[i], rel_tol=epsilon):
            return False
    return True

def gerar_matriz_dominante(ordem):
    matriz = np.zeros((ordem, ordem), dtype=float)
    for i in range(ordem):
        for j in range(ordem):
            matriz[i, j] = random.uniform(1, 10) if i != j else 0
        matriz[i, i] = sum(abs(matriz[i, :])) + random.uniform(1, 10)
    return matriz

def gerar_vetor(ordem):
    return np.array([random.uniform(1, 100) for _ in range(ordem)], dtype=float)

# ----------- Configuração -----------

epsilon = 1e-8

# Exemplo de matriz e vetor fixos
M = np.array([[3, 2, 4], [0, 1/3, 2/3], [0, 0, -8]], dtype=float)
c = np.array([1, 5/3, 0], dtype=float)

# Ou matriz gerada aleatoriamente
# ordem = 3
# M = gerar_matriz_dominante(ordem)
# c = gerar_vetor(ordem)

print("Matriz M:\n", M)
print("\nVetor c:\n", c)

# ----------- Verificações -----------

if not possui_diagonal_dominante(M):
    print("A matriz não possui diagonal dominante, resultados podem ser imprecisos.")

if verificar_zero_diagonal(M):
    print("A matriz contém zero na diagonal principal. Tente outra matriz.")
else:
    if verificar_vetor_constante(c):
        print("Todos os valores do vetor c são iguais. Tente outro vetor.")
    elif np.linalg.det(M) == 0:
        print("O determinante da matriz é zero. Não há solução.")
    else:
        x0 = np.zeros_like(c)  # Vetor inicial
        solucao, iteracoes = metodo_gauss_jacobi(M, c, x0, epsilon)

        print("\nSolução encontrada:", solucao)
        print("Número de iterações:", iteracoes)
        print("As raízes são válidas?", validar_raizes(M, c, solucao, epsilon))
