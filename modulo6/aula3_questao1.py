print("Digite os números da lista('fim' para encerrá-la)")
l1 = []
l2 = []
l3 = []
numeros = 0
while True:
    x = input("")
    if x == "fim" and numeros >= 4: break
    try:
        valor = int(x)
        l1.append(valor)
        numeros += 1
        if x % 2 == 0:
            l2.append(x)
        else:
            l3.append(x)
     
print(l1)
print(l1[0:4])
print(l1[::-1])
print(l2)
print(l3)