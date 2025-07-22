n = int(input("Digite o número de experimentos:"))
s = 0
r = 0
c = 0
while n > 0:
    x = int(input("Digite a quantidade de cobaias:"))
    y = (input("Digite o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho):"))
    if y == "S":
        s = s + x
    elif y == "R":
        r = r + x
    elif y == "C":
        c = c + x
    n = n - 1
total = s + r + c
print(f"Total de cobaias:{total}")
print(f"Total de coelhos:{c}")
print(f"Total de ratos:{r}")
print(f"Total de sapos:{s}")
c = (c/total) * 100
r = (r/total) * 100
s = (s/total) * 100
print(f"Percentual de coelhos:{c}")
print(f"Percentual de ratos:{r}")
print(f"Percentual de sapos:{s}")