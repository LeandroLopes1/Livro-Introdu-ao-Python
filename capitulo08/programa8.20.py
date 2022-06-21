import random

n = random.randint(0, 10)
tentativas = 0
while tentativas < 3:
    x = int(input("Digite um número entre 0 e 10: "))
    if x == n:
        print("Parabéns, você acertou!")
        break
    else:
        print(f"Você errou!")
        tentativas += 1
else:
    print(f"Você errou! O número era {n}")

