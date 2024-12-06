'''
4ª Questão: Implemente o método da falsa posição usando a linguagem de
programação Python. O algoritmo deve fornecer como resposta se uma
função escolhida pelo usuário possui ou não raiz em um intervalo [a, b]
escolhido também pelo usuário. Cuide para que seu algoritmo analise todas
as possibilidades acerca da escolha da raiz. Meça também o tempo de
execução e compare com o método da bissecção e a quantidade de iterações
necessárias para encontrar a raiz.
'''

import math

def f(x):
    return x ** 2 + 1

eps = 0.0001

def fp(a, b, k):    
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    
    if abs(f(a)) < eps:
        return a
    elif abs(f(b)) < eps:
        return b
    
    if k < 0:
        return None
    
    if abs(f(c)) < eps:
        return c
    

    if f(a) * f(c) < 0:
        return fp(a, c, k-1)
    elif f(c) * f(b) < 0:
        return fp(c, b, k-1)
    
    r1 = fp(a, c, k-1)
    r2 = fp(c, b, k-1)
    
    if r1 is None:
        return r2
    elif r2 is None:
        return r1
    else:
       return min(abs(f(r1)), abs(f(r2)))
    
    
print(fp(2,4,50))