def decomposicao_LU_Crout(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for k in range(n):
        # Calcula os elementos de L
        for i in range(k, n):
            soma = sum(L[i][p] * U[p][k] for p in range(k))
            L[i][k] = A[i][k] - soma
        
        # Define a diagonal principal de U como 1
        U[k][k] = 1.0

        # Calcula os elementos de U
        for j in range(k + 1, n):
            soma = sum(L[k][p] * U[p][j] for p in range(k))
            U[k][j] = (A[k][j] - soma) / L[k][k]

    return L, U

def substituicao_direta(L, b):
    """
    Resolve o sistema L * y = b por substituição direta.
    """
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        soma = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - soma) / L[i][i]
    return y

def substituicao_retroativa(U, y):
    """
    Resolve o sistema U * x = y por substituição retroativa.
    """
    n = len(U)
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        soma = sum(U[i][j] * x[j] for j in range(i+1, n))
        x[i] = y[i] - soma
    return x

def sistema_LU(A, b):
    # Decomposição LU
    L, U = decomposicao_LU_Crout(A)
    print("Matriz L:")
    for linha in L:
        print(linha)
    print("Matriz U:")
    for linha in U:
        print(linha)
    
    # Resolve L * y = b
    y = substituicao_direta(L, b)
    # Resolve U * x = y
    x = substituicao_retroativa(U, y)
    return x

print("TESTE 01 - 3x3\n 2x + 3y - z = 5\n 4x + 4y - 3z = 3\n 2x - 3y + z = -1\n")
# TESTE 01
A = [[2, 3, -1],
     [4, 4, -3],
     [2, -3, 1]] 
b = [5, 3, -1]

res = sistema_LU(A, b)
print("Solução do sistema:", res, "\n")

print("TESTE 02 - 3x3\n 2x - y + z = 3\n -4x + 6y = 9\n -4x - 2y + 8z = -6\n")
# TESTE 02
A = [[2, -1, 1],
     [-4, 6, 0],
     [-4, -2, 8]] 
b = [3, 9, -6]

res = sistema_LU(A, b)
print("Solução do sistema:", res)