import math, random
s = 0
n1 = int(input("Digite a quantidade de valores: "))
for n in range(n1):
    r = random.randint(0, 100)
    s = r + s
print(math.sqrt(s))

    