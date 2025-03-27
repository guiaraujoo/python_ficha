def divisivel(num1,num2): 
    if num2 == 0: 
        return "err0"
   
    if num1 % num2 == 0: 
        return True 
    else:
        return False
    

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num2 == 0:
    print("O segundo número não pode ser 0")
    exit() 
if divisivel(num1,num2) == True: 
    print(f"O número {num1} é divisível por {num2}")
else:
    print(f"O número {num1} não é divisível por {num2}")