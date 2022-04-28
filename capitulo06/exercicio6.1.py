notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 7:
    notas[x] = float(input("Digite a nota: "))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print(f"Nota {x}: {notas[x]:.2f}")
    x += 1
print(f"Média: {soma / 7:.2f}")