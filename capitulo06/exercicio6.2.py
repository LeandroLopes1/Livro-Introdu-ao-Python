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
terceira = primeira[:] # Copia a lista primeira para a lista terceira
terceira.extend(segunda) # Adiciona os elementos da lista segunda a lista terceira
x = 0 # Contador
while x < len(terceira): # Enquanto o contador for menor que o tamanho da lista terceira
    print(terceira[x]) # Imprime o elemento da lista terceira na posição do contador
    x += 1 # Incrementa o contador