frase = input("Digite uma frase: ")
consoantes = []
vogais = [n if n == "a" or n == "e" or n == "i" or n == "o" or n == "u" or n == "A" or n == "E" or n == "I" or n == "O" or n == "U" else consoantes.append(n) for n in frase]
for n in vogais:
    if n == None:
        vogais.remove(n)
print(vogais)
print(consoantes)
