def vogais(letra):
    vogal = ["a", "e", "i", "o", "u"]
    if len(letra) != 1:  
        return 0  
    return 1 if letra.lower() in vogal else 0


letra = input("Digite uma letra: ")
print(vogais(letra)) 