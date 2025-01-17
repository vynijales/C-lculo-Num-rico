import numpy as np
from Q2 import triangular_superior

def eliminacao_de_gauss(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)

    # Etapa de eliminação
    for k in range(n - 1):
        # Verifica se o pivô é zero e realiza a troca de linha
        if A[k, k] == 0:
            for i in range(k + 1, n):
                if A[i, k] != 0:
                    # Troca as linhas k e i em A e b
                    A[[k, i]] = A[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break
            else:
                raise ValueError("Sistema não tem solução única devido a pivô nulo.")
            
        for i in range(k + 1, n):
            # Calcula o fator de multiplicação m para zerar o elemento A[i, k]
            m = A[i, k] / A[k, k]
            A[i, k] = 0  # Zera o elemento abaixo do pivô
            
            # Atualiza o restante dos elementos da linha i
            for j in range(k + 1, n):
                A[i, j] -= m * A[k, j] # Atualiza a linha i da matriz A
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
    A = np.array(
        [[0, 4, -1],
        [-7, 7, 4],
        [5, 2, -5]]
        )

    b = np.array([4, -8, 9])
    
    # Solução do sistema
    x = eliminacao_de_gauss(A, b)
    print("Solução do sistema:", x)
