def media(n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    return media

n1 = int(input("Digite sua primeira nota:"))
n2 = int(input("Digite sua segunda nota: "))
n3 = int(input("Digite sua terceira nota:"))

resultado = media(n1, n2, n3)
print("A média do aluno foi:", resultado)