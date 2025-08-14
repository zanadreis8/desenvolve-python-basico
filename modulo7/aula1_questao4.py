numero = input("Digite o número: ")
primeiro_numero = False
if len(numero) == 8:
    numero = "9" + numero
    primeiro_numero = True
elif numero[0] == 9:
    primeiro_numero = True
else:
    print("Número inválido: com 9 dígitos o primeiro deve ser 9")    
numero = numero[:5] + "-" + numero[5:]
print(numero)