import csv
import numpy as np
import matplotlib.pyplot as plt
import math

# avalia o polinomio interpolador usando polinomios de Lagrange
def interpolL(x,T):
    Soma=0
    for i in range(len(T)):
        produto=1.0
        
        for j in range(len(T)):
            if j==i: continue
            produto=produto*(x-T[j][0])/(T[i][0]-T[j][0])
        
        Soma=Soma+T[i][1]*produto

    return Soma

T = []

# Coloca os dados do .csv na matriz T
with open('prova2/pontosQ8b.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    pulaLinha1 = True

    for row in spamreader:

        # Pula a linha que tem as letras 'x' e 'y'
        if pulaLinha1:
            pulaLinha1 = False
            continue

        result = row[0].split(',')
        T.append((float(result[0]), float(result[1])))

# função para calcular o limitante (é especifica para função da questão)
def calc_limitante(x, T):

    # A formula do limitante é E_n(x) = (f^(n+1)(ξ))/(n+1)! * ((|x-x_0|) * ... * (|x-x_n|))
    # E_n(x) = derivada_n+1(ξ)/(n+1)! * produtorio(x - x_i), i = 0 .. n

    ξ = max(T)[0] # Maior ponto no intervalo para garantir o valor máximo da derivada (levando em conta que a função é e^x).

    derivada = math.exp(ξ) # A função é e^x, logo a derivada em qualquer grau sempre será e^x.

    fatorial = math.factorial(len(T)) # fatorial de n+1 (polinomio de grau 2 -> n=2, sendo n+1 a quantidade de pontos)

    produtorio = 1 # inicializando variavel

    for i in range(len(T)):
        produtorio *= (x - T[i][0]) # cálculo do produtorio (x - x_i), i = 0 .. n

    return (derivada/fatorial)*abs(produtorio) # cálculo do limitante com a formula

x_alvo = 3.1 # ponto alvo

limitante = calc_limitante(x_alvo, T) # limitante do erro no ponto alvo

# define o polinomio interpolador p(x)
p= lambda x: interpolL(x,T) 

print(p(x_alvo))
print(math.e**x_alvo)
print(limitante) # resposta final
