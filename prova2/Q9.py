import numpy as np

def calc(X, Y, x):
  soma = 0

  for i in range(len(X)):
    produto = 1
    for j in range(len(Y)):
      if j == i: continue
      produto *= (x - X[j])/(X[i] - X[j])

    soma += Y[i] * produto
  
  return soma
  
# Numero dos meses
meses = [1, 2, 3, 5, 6]  
mes_abril = 4
mes_julho = 7

#Inflação
inflacao = [0.75, 0.64, 0.24, 2.94, 0.37]

# (a) Estime qual foi a inflação em abril, utilizando o polinômio interpolador de grau n <= 2.
inf_abril = calc(meses[2:5], inflacao[2:5], mes_abril)
print(f"(a) Estimativa da inflação em abril: {inf_abril:.2f}%")

# (b) Calcule o erro da estimativa anterior.
inf_abril_4 = calc(meses, inflacao, mes_abril)
erro = abs(inf_abril_4 - inf_abril)
print(f"(b) Erro da estimativa em abril: {erro:.2f}%")

# (c) Podemos garantir, usando  o resultado do item anterior, que a inflação semestral foi menor que 6%?
semestral = np.sum(inflacao) + inf_abril
print(f"(c) Inflação semestral: {semestral:.2f}%")

# (d) Determine a inflação do mês de julho, usando o polinômio de grau n <= 2.
inf_julho = calc(meses[2:5], inflacao[2:5], mes_julho)
print(f"(d) Inflação em julho: {inf_julho:.2f}%")
