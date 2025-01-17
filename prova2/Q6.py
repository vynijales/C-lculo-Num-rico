import numpy as np

# Matrizes e vetores de entrada
matriz_a = np.array(((1, -1), (1, -1.00001)))
matriz_a_ajustada = np.array(((1, -1), (1, -0.99999)))

vetor_b = np.array((1, 0))

# Questão a
print("Resultados da Questão a)\n")

solucao_a = np.linalg.solve(matriz_a, vetor_b)
determinante_a = np.linalg.det(matriz_a)
condicionamento_a = np.linalg.cond(matriz_a)

solucao_a_ajustada = np.linalg.solve(matriz_a_ajustada, vetor_b)
determinante_a_ajustada = np.linalg.det(matriz_a_ajustada)
condicionamento_a_ajustada = np.linalg.cond(matriz_a_ajustada)

print(f"Solução para matriz A: {solucao_a}")
print(f"Determinante de A: {determinante_a}")
print(f"Número de condicionamento de A: {condicionamento_a}")

print("\n---\n")

print(f"Solução para matriz A ajustada: {solucao_a_ajustada}")
print(f"Determinante de A ajustada: {determinante_a_ajustada}")
print(f"Número de condicionamento de A ajustada: {condicionamento_a_ajustada}")

# Questão b
print("\n\nResultados da Questão b)\n")

def calcular_condicionamento(tamanho):
    matriz_hilbert = np.zeros((tamanho, tamanho), dtype=float)
    vetor_h = np.ones((tamanho, 1), dtype=float)

    # Construção da matriz de Hilbert
    for linha in range(tamanho):
        for coluna in range(tamanho):
            matriz_hilbert[linha][coluna] = round(1 / (linha + coluna + 1), 5)

    print(f"Matriz de Hilbert (n={tamanho}):\n{matriz_hilbert}")
    
    determinante_h = np.linalg.det(matriz_hilbert)
    solucao_h = np.linalg.solve(matriz_hilbert, vetor_h)
    condicionamento_h = np.linalg.cond(matriz_hilbert)
    
    print(f"\nDeterminante da matriz de Hilbert: {determinante_h}")
    print(f"Solução do sistema para Hilbert: {solucao_h}")
    print(f"Número de condicionamento da matriz de Hilbert: {condicionamento_h}")

for dimensao in range(3, 11):
    calcular_condicionamento(dimensao)
    print("\n---\n")
