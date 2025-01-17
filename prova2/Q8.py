import numpy as np

def lagrange(x,T):
  Soma=0
  for i in range(len(T)):
    produto=1.0
    for j in range(len(T)):
      if j==i: continue
      produto=produto*(x-T[j][0])/(T[i][0]-T[j][0])
    Soma=Soma+T[i][1]*produto
  return Soma

# A
def f(x):
    return np.exp(x)

# Pontos utilizados para aproximacão: 3.0, 3.1, 3.3
T = (
    (3, f(3)),
    (3.2, f(3.2)),
    (3.3, f(3.3))
)

x = 3.1

res = lagrange(x, T)
erro_absoluto = abs(np.exp(3.1) - res)
erro_relativo = (erro_absoluto / np.exp(3.1)) * 100

print("==== Letra A =====")
print(f"Valor Calculado com o Polinômio de Lagrange: {res}\nValor Real: {np.exp(3.1)}")
print(f"Erro absoluto: {erro_absoluto}\nErro Relativo: {erro_relativo}%")


# B
# Valores da tabela fornecida
x = [2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8]
y = [11.02, 13.46, 16.44, 20.08, 24.53, 29.96, 36.59, 44.70]

# Função exata para comparação (e^x)
def f(x):
    return np.exp(x)

# Valores exatos para os pontos fornecidos
y_exato = [f(x) for x in x]

# Erros entre os valores fornecidos e os valores exatos
erros = [abs(y_ex - y_tab) for y_ex, y_tab in zip(y_exato, y)]

# Encontrando o erro máximo
erro_max = max(erros)

print("==== Letra B =====")
print(f"O erro máximo cometido é: {erro_max:.4f}")
