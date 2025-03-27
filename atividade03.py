
def soma(num1, num2):
    return num1 + num2
def subtracao(num1, num2):
    return num1 - num2
def multiplicacao(num1, num2):
    return num1 * num2
def divisao(num1, num2 ):
    return num1 / num2

while True:
        print("\nMenu de Operações:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == '1':
            resultado = soma()
            print(f"Resultado: {resultado}")
        elif opcao == '2':
            resultado = subtracao()
            print(f"Resultado: {resultado}")
        elif opcao == '3':
            resultado = multiplicacao()
            print(f"Resultado: {resultado}")
        elif opcao == '4':
            resultado = divisao()
            print(f"Resultado: {resultado}")
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

