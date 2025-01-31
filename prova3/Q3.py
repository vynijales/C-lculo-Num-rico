def f(x):
    return x ** 2

def boole_repetida(f, a, b, n=4):
    if not n % 4 == 0:
        raise ValueError("O valor de n deve ser divisível por 4")

    h = (b - a) / n

    # Calcula os somatórios
    somatorio_32 = sum(f(a + h * i) for i in range(1, n, 2))
    somatorio_12 = sum(f(a + h * i) for i in range(2, n, 4))
    somatorio_14 = sum(f(a + h * i) for i in range(4, n, 4))
    
    # Aplica a fórmula
    return (2 * h / 45) * \
            (7 * (f(a) + f(b)) + \
            32 * somatorio_32 + \
            12 * somatorio_12 + \
            14 * somatorio_14)


print(boole_repetida(f, 1, 3, 8)) # 8.6666