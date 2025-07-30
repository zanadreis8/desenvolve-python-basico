import random
lista1 = []
lista2 = []
lista3 = []
for i in range(20):
    lista1 = lista1 + [random.randint(0,50)]
    lista2 = lista2 + [random.randint(0,50)]
print(sorted(lista1))
print(sorted(lista2))
for c in lista1:
    if c in lista2 and c not in lista3:
        lista3 = lista3 + [c]
print(f"Interseção: {sorted(lista3)}")
for c in lista1:
    if c in lista2:        
        a = lista1.count(c) 
        b = lista2.count(c)
        print(f"{c}: lista1= {a} lista2= {b}")