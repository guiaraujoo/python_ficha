def raizquadrada():
    numero = int(input("Qual o número? "))
    raiz = numero ** 0.5 
    if int(raiz) == raiz: 
        print(f"Tem raiz exata: {raiz}")
        return 1
    else:
        print("Não tem raiz exata")
        return 0

raizquadrada()