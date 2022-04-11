numero01 = int(input("Digite um número: "))
numero02 = int(input("Digite outro número: "))
operação = input("Digite a operação (+, -, *, /): ")
if operação == "+":
    resultado = numero01 + numero02
elif operação == "-":
    resultado = numero01 - numero02
elif operação == "*":
    resultado = numero01 * numero02
elif operação == "/":
    resultado = numero01 / numero02
else:
    print("Operação inválida")
    resultado = 0
print(f"O resultado da operação é {resultado}")