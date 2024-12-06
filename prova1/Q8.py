import math

# Dados do problema
S = 1200  # Área superficial em m²
h = 20    # Altura em metros
pi = math.pi

# Função de iteração g(r)
def g(r):
    return S / (pi * math.sqrt(r**2 + h**2))

# Método do ponto fixo
def ponto_fixo(r_inicial, iteracoes):
    r = r_inicial
    print(f"Iteração 0: r = {r:.6f}")
    for i in range(1, iteracoes + 1):
        r = g(r)
        print(f"Iteração {i}: r = {r:.6f}")
    return r

# Ponto inicial
r_inicial = 17  # Ponto inicial fornecido no problema
iteracoes = 5   # Número de iterações

# Calcular o raio aproximado
raio_aproximado = ponto_fixo(r_inicial, iteracoes)
print(f"\nRaio aproximado após {iteracoes} iterações: {raio_aproximado:.6f} metros")
