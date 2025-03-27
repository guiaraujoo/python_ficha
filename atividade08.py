def resto(n1,n2):
    r = n1 % n2
    return r

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

print(f"O resto da divisão de {n1} por {n2} é {resto(n1, n2)}")