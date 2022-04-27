dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente += 1
resto = x
print(f"O quociente é {quociente} e o resto é {resto}")
