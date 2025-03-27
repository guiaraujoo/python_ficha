def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um número: "))  # Recebe o input separadamente
print(f"O fatorial de {numero} é {fatorial(numero)}")  # Chama a função com o número digitado