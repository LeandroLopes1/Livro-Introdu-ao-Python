pares = open("pares.txt", "r")
saida = open("pares_invertidos.txt", "w")

L = pares.readlines()
L.reverse()
for i in L:
    saida.write(i)

pares.close()
saida.close()
