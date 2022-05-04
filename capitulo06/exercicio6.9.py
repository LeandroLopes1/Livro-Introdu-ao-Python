L = [15, 7, 27, 39]
p = int(input("Digite um valor a procurar: "))
v = int(input("Digite o segundo valor a procurar "))
x = 0
achouP = False
achouV = False
primeiro = 0
while x < len(L):
    if L[x] == p:
        achouP = True
        if not achouV:
            primeiro = 1
    if L[x] == v:
        achouV = True
        if not achouP:
            primeiro = 2
    x += 1
if achouP:
    print(f"p: {p} encontrado")
else:
    print(f"p: {p} não encontrado")
if achouV:
    print(f"v: {v} encontrado")
else:
    print(f"v: {v} não encontrado")
if primeiro == 1:
    print(f"p foi encontrado antes de v")
elif primeiro == 2:
    print(f"v foi encontrado antes de p")

