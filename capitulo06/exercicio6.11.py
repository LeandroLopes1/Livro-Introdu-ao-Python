L = []
while True:
    n = int(input("Digite um valor: (0 para sair) "))
    if n == 0:
        break
    L.append(n)
    for i in L:
        print(f"{i}")

# o while True é para que o programa não pare de imediatamente
# o for i in L é para que o programa percorra toda a lista
# ou seja, while não pode ser substituido por for, pois o numero de 
# repetições é desconhecido no inicio do programa