'''
2ª Questão: Faça um código em Python para discretizar as derivadas de
ordem 1, 2 e 3 de quatro maneiras diferentes para uma única função a ser
escolhida pelo usuário. O ponto em que a derivada vai ser calculada fica a
critério do usuário. Calcule também o erro percentual em cada cálculo de
derivada realizado.
'''

def discretizar_derivadas():
    def f(x):
        """Define a função escolhida pelo usuário."""
        return eval(funcao)  # Avalia a função com base na entrada do usuário.

    def derivada_analitica(x, ordem):
        """Define a derivada analítica da função para comparação."""
        return eval(derivadas_analiticas[ordem - 1])

    def erro_percentual(valor_aproximado, valor_exato):
        """Calcula o erro percentual entre o valor aproximado e o exato."""
        if abs(valor_exato) < 1e-10:  # Trata casos de valor analítico muito próximo de zero
            return float('inf') if abs(valor_aproximado) > 1e-10 else 0
        return abs((valor_aproximado - valor_exato) / valor_exato) * 100

    # Solicitar a função e derivadas analíticas do usuário
    funcao = input("Digite a função em termos de x (exemplo: x**3 - 2*x + 1): ")
    derivadas_analiticas = [
        input("Digite a expressão da derivada de ordem 1 (exemplo: 3*x**2 - 2): "),
        input("Digite a expressão da derivada de ordem 2 (exemplo: 6*x): "),
        input("Digite a expressão da derivada de ordem 3 (exemplo: 6): "),
    ]

    # Solicitar ponto e passo
    x0 = float(input("Digite o ponto onde deseja calcular as derivadas: "))
    h = float(input("Digite o valor do passo (h): "))

    # Validar h para evitar problemas numéricos
    if h <= 0:
        raise ValueError("O valor de h deve ser positivo.")
    if h < 1e-5:
        print("Aviso: Valores de h muito pequenos podem levar a erros numéricos.")

    # Métodos para calcular derivadas
    resultados = {"1ª ordem": [], "2ª ordem": [], "3ª ordem": []}

    # Derivada de 1ª ordem
    primeira_analitica = derivada_analitica(x0, 1)
    metodos_primeira = [
        (f(x0 + h) - f(x0)) / h,  # Diferenças progressivas
        (f(x0) - f(x0 - h)) / h,  # Diferenças retroativas
        (f(x0 + h) - f(x0 - h)) / (2 * h),  # Diferenças centradas
        (-3 * f(x0) + 4 * f(x0 + h) - f(x0 + 2 * h)) / (2 * h),  # Método avançado de 3 pontos
    ]

    for metodo in metodos_primeira:
        erro = erro_percentual(metodo, primeira_analitica)
        resultados["1ª ordem"].append((metodo, erro))

    # Derivada de 2ª ordem
    segunda_analitica = derivada_analitica(x0, 2)
    metodos_segunda = [
        (f(x0 + h) - 2 * f(x0) + f(x0 - h)) / h**2,  # Fórmula padrão
        (f(x0 + 2 * h) - 2 * f(x0 + h) + f(x0)) / h**2,  # Diferenças progressivas
        (f(x0 - 2 * h) - 2 * f(x0 - h) + f(x0)) / h**2,  # Diferenças retroativas
        (f(x0 + h) - 2 * f(x0) + f(x0 - h)) / h**2,  # Diferenças centradas
    ]

    for metodo in metodos_segunda:
        erro = erro_percentual(metodo, segunda_analitica)
        resultados["2ª ordem"].append((metodo, erro))

    # Derivada de 3ª ordem
    terceira_analitica = derivada_analitica(x0, 3)
    metodos_terceira = [
        (f(x0 + 2 * h) - 2 * f(x0 + h) + 2 * f(x0 - h) - f(x0 - 2 * h)) / (2 * h**3),  # Diferença combinada
        (f(x0 + 3 * h) - 3 * f(x0 + 2 * h) + 3 * f(x0 + h) - f(x0)) / h**3,  # Diferenças progressivas
        (-f(x0 + 3 * h) + 3 * f(x0 + 2 * h) - 3 * f(x0 + h) + f(x0)) / h**3,  # Diferença progressiva de 4 pontos
        (f(x0 + 2 * h) - 2 * f(x0 + h) + 2 * f(x0 - h) - f(x0 - 2 * h)) / h**3,  # Diferença combinada refinada
    ]

    for metodo in metodos_terceira:
        erro = erro_percentual(metodo, terceira_analitica)
        resultados["3ª ordem"].append((metodo, erro))

    # Exibir resultados
    for ordem, valores in resultados.items():
        print(f"\n{ordem}:")
        for i, (valor, erro) in enumerate(valores, 1):
            print(f"Método {i}: Valor = {valor:.6f}, Erro = {erro:.2f}%")

# Chamada principal
discretizar_derivadas()
