salario = float(input("Digite o salário para calculo do imposto: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto  + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"Salario: R$ {salario: 6.2f} \nImposto: R$ {imposto: 6.2f}")