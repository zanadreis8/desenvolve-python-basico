n = int(input("Digite a quantidade de respondentes:"))
z = n
y = 0
while n > 0:
    x = int(input("Digite a idade:"))
    y = y + x
    n = n - 1
print(y / z)