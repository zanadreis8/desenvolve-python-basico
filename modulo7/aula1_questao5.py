frase = input("Digite uma frase: ")
vogais = 0
indice = []
for i, n in enumerate(frase):
    if n in "aeiouAEIOU":
        vogais += 1
        indice.append(i)
print(vogais)     
print(indice)