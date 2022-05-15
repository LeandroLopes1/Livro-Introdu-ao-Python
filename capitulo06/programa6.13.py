lugares_vazios = [10, 2, 1, 3, 0]
while True:
    sala = int(input("Sala (0 para sair): "))
    if sala == 0:
        print("Fim do programa")
        break
    if sala > len(lugares_vazios) or sala < 1:
        print("Sala inválida")
    elif lugares_vazios[sala - 1] == 0:
        print("Sala lotada")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vazios[sala - 1]} vagos:) "))
        if lugares > lugares_vazios[sala - 1]:
            print("Quantidade de lugares inválida")
        else:
            lugares_vazios[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
    print("Utilização das salas")
    for i, x in enumerate(lugares_vazios):
        print(f"Sala {i + 1}: {x} lugares vazios")
