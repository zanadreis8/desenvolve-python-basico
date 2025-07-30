import random
num_elementos = random.randint(5,20)
elementos = []
print(num_elementos)
for i in range(num_elementos):
    x = random.randint(1,10)
    elementos = elementos + [x]
print(elementos)
print(sum(elementos))
print(sum(elementos) / num_elementos)