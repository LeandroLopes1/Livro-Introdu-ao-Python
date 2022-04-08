salario = float(input("Digite o salário: "))
procentagem_aumento = float(input("Digite a porcentagem de aumento: "))
aumento = salario * procentagem_aumento / 100
print(f"O aumento é de: {aumento:.2f}")
print(f"O novo salário é de: {salario + aumento:.2f}")