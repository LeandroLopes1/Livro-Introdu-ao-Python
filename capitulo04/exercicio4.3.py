numero01 = int(input("Digite um número: "))
numero02 = int(input("Digite outro número: "))
numero03 = int(input("Digite mais um número: "))

maior = numero01
if numero02 > maior:
    maior = numero02
if numero03 > maior:
    maior = numero03

menor = numero01
if numero02 < menor:
    menor = numero02
if numero03 < menor:
    menor = numero03

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
