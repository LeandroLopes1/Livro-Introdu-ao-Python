L = [15, 7, 27, 39]
p = int(input("Digite um valor a procurar: "))
v = int(input("Digite o segundo valor a procurar "))
x = 0
achouP = -1
achouV = -1
primeiro = 0
while x < len(L):
    if L[x] == p:
        achouP = x
        if achouV == -1:
            primeiro = 1
    if L[x] == v:
        achouV = x
        if achouP == -1:
            primeiro = 2
    x += 1
if achouP != -1:
    print(f"p: {p} encontrado na posição {achouP}")
else:
    print(f"p: {p} não encontrado")
if achouV != -1:
    print(f"v: {v} encontrado na posição {achouV}")
else:
    print(f"v: {v} não encontrado")
if primeiro == 1:
    print(f"p foi encontrado antes de v")
elif primeiro == 2:
    print(f"v foi encontrado antes de p")
