b = int(input("Forneça a base: "))
n = int(input("Forneça o numero na base 10: "))

if b < 2 or b > 36:
    print("Base inválida (deve estar entre 2-36)")
    exit()
    
def base(b,n):
    n = abs(n) # Valor absoluto
    digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while n > 0:
        r = n % b
        result = digitos[r] + result
        n = n // b
    return result

result = base(b,n)
result = result if n >= 0 else "-" + result
print(f"O numero {n} na base {b} é: {result}")
