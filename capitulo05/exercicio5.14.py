n = 0
soma = 0 

while True:
    numero_teclado = int(input("Digite um número: "))
    if numero_teclado == 0:
        break
    n += numero_teclado
    soma += 1
print(f"quantidade de números digitados: {soma}")
print(f"A soma de números digitados é {n}")
print(f"A média dos números digitados é {n/soma}")

