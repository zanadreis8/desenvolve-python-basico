ano = int(input("Digite o ano:"))
bissexto = (ano % 4 == 0) and (ano % 100 > 0) or (ano % 400 == 0)
if bissexto:
    print("Bissexto")
else:
    print("Não Bissexto")