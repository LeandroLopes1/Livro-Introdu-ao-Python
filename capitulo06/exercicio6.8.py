L = [15, 7, 27, 39]
p = int(input("Digite um valor a procurar: "))
x = 0
while x < len(L):
    if L[x] == p:
        print(f"O valor {p} está na posição {x}")
        break
    x += 1
else:
    print(f"O valor {p} não foi encontrado")
