import numpy as np
from Q2 import triangular_superior

def eliminacao_de_gauss(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)

    # Etapa de eliminação
    for k in range(n - 1):
        for i in range(k + 1, n):
            # Calcula o fator de multiplicação m para zerar o elemento A[i, k]
            m = A[i, k] / A[k, k]
            A[i, k] = 0  # Zera o elemento abaixo do pivô
            
            for j in range(k + 1, n):
                A[i, j] -= m * A[k, j] # Atualiza o restante dos elementos da linha i
            b[i] -= m * b[k] # Atualiza o vetor b
    
    # Resolve o sistema triangular superior (função da Q2)
    x = triangular_superior(A, b)
    
    return x

if __name__ == "__main__":
    '''# Teste 1
    A = np.array([[3, -0.1, -0.2],
                  [0.1, 7, -0.3],
                  [0.3, -0.2, 10]])
    b = np.array([7.85, -19.3, 71.4])'''
    
    # Teste 2
    A = np.array([[2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]])

    b = np.array([8, -11, -3])
    
    # Solução do sistema
    x = eliminacao_de_gauss(A, b)
    print("Solução do sistema:", x)
