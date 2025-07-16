dist = int(input("Digite a distância em km:"))
peso = int(input("Digite o peso do pacote em kg:"))
if dist <= 100:
    valor = 1
if dist > 100 and dist <= 300:
    valor = 1.5
if dist > 300:
    valor = 2
valor_final = valor * peso
if peso > 10:
    valor_final = valor_final + 10
print(f"O valor do frete é: {valor_final}R$")