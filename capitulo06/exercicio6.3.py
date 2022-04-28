primeira = []
segunda = []
while True:
    e = int(input("Digite um valor para a primeira lista(0 para sair): "))
    if e == 0:
        break
    primeira.append(e)
while True:
    e = int(input("Digite um valor para a segunda lista(0 para sair): "))
    if e == 0:
        break
    segunda.append(e)
terceira = []
duas_listas = primeira[:]
duas_listas.extend(segunda)
x = 0 # Contador
while x < len(duas_listas): # Enquanto o contador for menor que o tamanho da lista terceira
    y = 0 # Contador
    while y < len(terceira): # Enquanto o contador for menor que o tamanho da lista terceira
        if duas_listas[x] == terceira[y]: # Se o elemento da lista duas_listas na posição x for igual ao elemento da lista terceira na posição y
            break # Sai do laço
        y += 1 # Incrementa o contador
    if y == len(terceira): # Se o contador for igual ao tamanho da lista terceira
        terceira.append(duas_listas[x]) # Adiciona o elemento da lista duas_listas na posição x a lista terceira
    x += 1 # Incrementa o contador
x = 0 # Contador
while x < len(terceira): # Enquanto o contador for menor que o tamanho da lista terceira
    print(terceira[x]) # Imprime o elemento da lista terceira na posição do contador
    x += 1 # Incrementa o contador


""" lista_01 = [0, 1, 2, 4, 8]
lista_02 = [0, 3, 4, 5, 8]
lista_03 = []

lista_03 = lista_01[:]

for i in lista_02:
    if i not in lista_03:
        lista_03.append(i)

for i in lista_03:
    print(i) """
           