t1 = int(input("Digite a quantidade de elementos da lista 1: "))
t2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista1 = []
lista2 = []
print(f"Digite os {t1} elementos da lista 1:")
for i in range(t1):
    n = int(input())
    lista1 = lista1 + [n]
print(f"Digite os {t2} elementos da lista 2:")
for i in range(t2):
    n = int(input())
    lista2 = lista2 + [n]
print(lista1, lista2)
t3 = min(t1, t2)
lista3 = []
for i in range(t3):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
t4 = max(t1,t2)
lista4 = []
if t1 > t2 or t1 == t2:
    lista4 = lista1
else:
    lista4 = lista2
i = i + 1
for o in range(i, t4):
    lista3.append(lista4[o])
print(f"Lista intercalada: {lista3}")
