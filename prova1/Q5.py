''''
Calcular os limites
'''

import math

def f(x):
    if x == 0:
        return 0
    return x ** 4 * math.sin(1/x)

def g(x):
    if x > 1:
        return x ** 4 - 1
    elif x < 1:
        return (-1 * x) ** 4 + 1

x0 = 0
eps = 0.0001 # Precisão

for n in range(10000):
    direita = f(x0 + (1/(10+n**2)))
    esquerda = f(x0 - (1/(10+n**2)))


print("lim x->0 f(x)")
print(f"Limite pela direita: {direita}")
print(f"Limite pela esquerda: {esquerda}")

if abs(direita - esquerda) < eps:
    print(f"Limite bilateral: {direita}")


# Segundo limite
x0 = 1
eps = 0.0001 # Precisão

for n in range(10000):
    direita = g(x0 + (1/(10+n**2)))
    esquerda = g(x0 - (1/(10+n**2)))

print("lim x->1 g(x)")
print(f"Limite pela direita: {direita}")
print(f"Limite pela esquerda: {esquerda}")

if abs(direita - esquerda) < eps:
    print(f"Limite bilateral: {direita}")