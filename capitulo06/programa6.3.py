# Programa 6.3 - Apresentação de numeros

numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = int(input(f"Digite o {x + 1}º numero: "))
    x += 1
while True:
    escolhido = int(input("Digite a posição que você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print(f"O numero escolhido foi {numeros[escolhido - 1]}")