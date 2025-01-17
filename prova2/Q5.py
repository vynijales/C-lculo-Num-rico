import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=1000):
  """
  Resolve um sistema linear Ax = b usando o método de Gauss-Seidel.

  Parâmetros:
  A: matriz dos coeficientes do sistema
  b: vetor dos termos independentes
  x0: vetor inicial (opcional, default é um vetor de zeros)
  tol: tolerância para critério de convergência
  max_iter: número máximo de iterações

  Retorna:
  x: vetor que aproxima a solução do sistema
  iter_count: número de iterações realizadas
  """
  n = len(b)
  x0 = x0 if x0 is not None else [0.0] * n # Se x0 não for fornecido, inicia com um vetor de zeros
  x = x0.copy()

  for k in range(max_iter):
    x_old = x.copy()

    for i in range(n):
      sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
      x[i] = (b[i] - sigma) / A[i][i]

      # Critério de convergência
      if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
        return x, k + 1 # Retorna a solução e o número de iterações

  raise ValueError("O método de Gauss-Seidel não convergiu após o número máximo de iterações.")


# Critérios de Convergência
def criterio_linhas(A):
    """
    Verifica se a matriz é estritamente diagonal dominante
    """
    for i in range(len(A)):
        diagonal = abs(A[i][i])
        fora_da_diagonal_soma = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
        if diagonal <= fora_da_diagonal_soma:
            return False
    return True

def criterio_sassenfeld(A):
    """
    Critério de Sassenfeld
    """
    n = len(A)
    betas = [0] * n
    
    for i in range(n):
        diagonal = abs(A[i][i])
        if diagonal == 0:
            # Caso a diagonal principal tenha um zero, não é possível aplicar o método
            return False
        
        soma = sum(abs(A[i][j]) * betas[j] for j in range(n) if j != i)
        
        # Atualiza o beta para a linha atual
        betas[i] = soma / diagonal
        
        # Critério de Sassenfeld: se algum beta >= 1, não há convergência garantida
        if betas[i] >= 1:
            return False

    return True


def zero_na_diagonal(A):
  """
  Verifica se existe algum 0 na diagonal principal
  """
  for i in range(len(A)):
    if A[i][i] == 0:
      return True
  return False


# Exemplo de Uso
A = np.array([[4, -1, 0, 0],
[-1, 4, -1, 0],
[0, -1, 4, -1],
[0, 0, -1, 3]])

b = np.array([15, 10, 10, 10])

if np.linalg.det(A) == 0:
  print("A matriz nao possui solucão (Determinante = 0)")
elif zero_na_diagonal(A):
  print("A matriz possui zero na diagonal principal, portanto o método é inviável (divisão por 0)")
else:
  print("===== Critérios de Convergência =====")
  print(f"Critério das Linhas: {criterio_linhas(A)}")
  print(f"Critério de Sassenfeld: {criterio_sassenfeld(A)}")

  solution, iterations = gauss_seidel(A, b)

  print("Solução aproximada:", solution)
  print("Número de iterações:", iterations)
