def triangular_superior(A, b):
    n = len(b)  # Número de equações do sistema
    x = [0] * n  # Vetor solução
    
    # Calcula a última variável diretamente
    x[n-1] = b[n-1] / A[n-1][n-1]
    
    # Calcula as demais variáveis
    for k in range(n-2, -1, -1):  # k vai de n-2 até 0 (inclusive)
        s = 0
        
        # Calcula a soma dos termos já calculados
        for j in range(k+1, n):
            s += A[k][j] * x[j]
            
        x[k] = (b[k] - s) / A[k][k]
    
    return x

# Exemplo de uso
A = [[2, -1, 1],
     [0, 3, -2],
     [0, 0, 4]]

b = [2, 5, 8]

res = triangular_superior(A, b)
print("Solução do sistema:", res)