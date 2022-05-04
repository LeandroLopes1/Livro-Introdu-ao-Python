pilha = []
while True:
    print("Digite uma sequencia de parenteses para verificar se os parenteses foram fechados.")
    sequencia = input("Digite uma sequencia de parenteses: ")
    x = 0
    while x < len(sequencia):
        if sequencia[x] == "(":
            pilha.append(sequencia[x])
        elif sequencia[x] == ")":
            if len(pilha) == 0:
                print("Sequencia inválida!")
                break
            else:
                pilha.pop()
        x += 1
    if len(pilha) == 0:
        print("Sequencia válida!")
        break
    else:
        print("Sequencia inválida!")
        pilha = []
        continue
print("Fim do programa!")



""" expressão = input("Digite a sequencia de parenteses a validar: ")
x = 0
pilha = []
while x < len(expressão):
    if expressão[x] == "(":
        pilha.append("(")
    if expressão[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else :
            pilha.append(")")
            break
    x += 1
if len(pilha) == 0:
    print("Expressão válida!")
else:
    print("Expressão inválida!") """
