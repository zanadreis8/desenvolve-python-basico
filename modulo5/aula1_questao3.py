import random
n = random.randint(1,10)
print(n)
certo = True
while certo:
    palpite = int(input("Digite um número entre 1 e 10: "))
    if palpite == n:
        print(f"Correto! O número é {n}!")
        certo = False
    elif palpite < n:
        print("Muito baixo, tente novamente!")
    else:
        print("Muito alto, tente novamente!")