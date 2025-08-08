l1 = []
for n in range(20,51):
    l1.append(n)
pares = [n for n in l1 if n % 2 == 0]
print(pares)
l2 = [1,2,3,4,5,6,7,8,9]
quadrado = [n * n for n in l2 ]
print(quadrado)
l3 = []
for n in range(1, 101):
    l3.append(n)
d7 = [n for n in l3 if n % 7 == 0]
print(d7)
l4 = []
for n in range(0,30,3):
    l4.append(n)
paridade = ["par" if n % 2 == 0 else "impar" for n in l4]
print(paridade)