import random
lista = []
for i in range(20):
    a = random.randint(-100, 100)
    lista = lista + [a]
print(sorted(lista))
print(lista)
print(lista.index(max(lista)))
print(lista.index(min(lista)))