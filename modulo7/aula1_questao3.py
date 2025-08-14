frase = input("Digite a frase:")
espaço = 0
for i in frase:
    if i == " ":
        espaço += 1 
print(f"Espaços em branco: {espaço}")