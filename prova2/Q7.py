import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 7ª Questão: Implementar um algoritmo em Python para o polinômio de 
# Lagrange. Este algoritmo deve receber um arquivo e partir deste extrair os 
# valores de x e y para serem utilizados na construção do polinômio de 
# Lagrange.

# Avalia o polinomio interpolador usando polinomios de Lagrange
def interpolL(x,T):
    Soma=0
    for i in range(len(T)):
        produto=1.0
        for j in range(len(T)):
            if j==i: continue
            produto=produto*(x-T[j][0])/(T[i][0]-T[j][0])
            Soma=Soma+T[i][1]*produto
    return Soma

# Extrai os valores de um arquivo csv
def getT():
    T = []
    df = pd.read_csv('prova2/usina_solar.csv')
    for i in range(len(df)):
        T.append((df.iloc[i,0],df.iloc[i,1]))
    return T
    
def main():
    T = getT()

    print('Valores de energia gerada pela usina solar')
    print(T)

    p= lambda x: interpolL(x,T) # define o polinomio interpolador p(x)

    x=np.linspace(0,10,500)

    plt.figure(figsize=(5, 5))

    plt.plot(x,p(x), color='#FF4500', marker = '', linewidth=1.0)
    plt.title ('Estimativa dos valores gerados pela usina solar')
    plt.xlabel('Valores medidos em horas')
    plt.ylabel('Energia gerada em Kwh')

    print(p(9.7))

    plt.grid()

    plt.show()

if __name__ == '__main__':
    main()
