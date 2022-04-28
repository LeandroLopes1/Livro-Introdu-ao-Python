ultimo = 10
fila = list(range(1, ultimo + 1))
fila_02 = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila 01.")
    print(f"Fila atual 01: {fila}")
    print(f"\nExistem {len(fila_02)} clientes na fila 02.")
    print(f"Fila atual 02: {fila_02}\n")
    print("Digite F para adicionar um cliente ao fim da fila 01,")
    print("Digite G para adicionar um cliente ao fim da fila 02,")
    print("Digite A para realizar o atendimento na fila 01.")
    print("Digite B para realizar o atendimento na fila 02. S para sair.")
    operação = input("Operação (F, G, A, B ou S): ")
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia!, não há clientes para atender.")
        elif operação[x] == "F":
            ultimo += 1
            fila.append(ultimo)
        elif operação[x] == "G":
            ultimo += 1
            fila_02.append(ultimo)
        elif operação[x] == "B":
            if len(fila_02) > 0:
                atendido = fila_02.pop(0)
                print(f"Cliente {atendido} atendido.")
            else:
                print("Fila vazia!, não há clientes para atender.")
        elif operação[x] == "S":
            sair = True
            break
        else:
            print("Operação inválida! Digite apenas F, G, A, B ou S.")
        x += 1
    if sair:
        break
