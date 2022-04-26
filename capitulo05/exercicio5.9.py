primeiro_numero = int(input("Digite o dividendo: "))
segundo_numero = int(input("Digite o divisor: "))

resultado = 0
x = primeiro_numero

while x >= segundo_numero:
    x = x - segundo_numero
    resultado = resultado + 1
resto = x

print(f"{primeiro_numero} / {segundo_numero} = {resultado} resto {resto}")