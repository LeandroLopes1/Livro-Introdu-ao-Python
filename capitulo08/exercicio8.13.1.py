import random

n = random.randint(0, 10)
x = int(input("Digite um número entre 0 e 10: "))
if x == n:
    print("Parabéns, você acertou!")
else:
    print(f"Você errou! O número era {n}")