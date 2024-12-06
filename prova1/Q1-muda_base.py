# 1ª Questão: Escreva um código em Python que faça a mudança de base de 
# um  número  escrito  na  base  dez  para  um  número  escrito  em  uma  base  a 
# critério do usuário.

def get_valid_base() -> int:
    while True:
        try:
            base = int(input("Forneça uma base (deve estar entre 2-36): "))
            if 2 <= base <= 36:
                return base
            else:
                print("Base inválida (deve estar entre 2-36)")
        except ValueError:
            print("Base inválida (deve ser um número inteiro)")

def converter_base(numero: str, base_destino: int = 10) -> str:
    base_origem = 10
    try:
        decimal = abs(int(numero, base_origem)) # Verifica e é na base 10
    except ValueError:
        raise ValueError(f"O número {numero} não é válido na base {base_origem}")
    
    # Converter do decimal para a base destino
    if base_destino == 10:
        return str(decimal)
    else:
        alfabeto = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        while decimal > 0:
            resto = decimal % base_destino
            resultado = alfabeto[resto] + resultado
            decimal //= base_destino
        return resultado or "0"

def main():
    numero = input("Forneça o número na base 10: ")
    base = get_valid_base() # Solicita uma base válida para conversão

    numero_convertido = converter_base(numero, base)
    print(f"O número {numero} na base 10 convertido para a base {base} é: {numero_convertido}")

if __name__ == "__main__":
    main()
