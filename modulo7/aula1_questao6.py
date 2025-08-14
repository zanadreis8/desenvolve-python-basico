frase = input("Digite uma frase: ")
obj = sorted("amor")
lista = frase.lower().split()
for palavra in lista:
    if sorted(palavra) == obj:
        print(palavra)