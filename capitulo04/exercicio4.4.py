salario = float(input("Digite seu Sálario: "))
if salario > 1250:
    salario = salario + salario * 0.10 
    print(f"Seu salario com 10% de aumento é: R$ {salario:.2f}")
if salario < 1250:
    salario = salario + salario * 0.15
    print(f"Seu salario com 15% de aumento é: R$ {salario:.2f}")