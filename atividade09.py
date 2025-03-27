def menor(n1,n2,n3):
    if n1 < n2 and n1 < n3:
        return n1
    if n2 < n1 and n2 < n3:
        return n2
    if n3 < n1 and n3 < n2:
        return n3
    
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

print(f"O menor número é {menor(n1, n2, n3)}")