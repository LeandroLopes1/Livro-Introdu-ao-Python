primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))

x = 1
resultado = 0

while x <= segundo_numero:
    resultado = resultado + primeiro_numero
    x = x + 1
print(f"{primeiro_numero} x {segundo_numero} = {resultado}")
