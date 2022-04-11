valor_casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Digite o salário do comprador: "))
anos_para_pagar = int(input("Digite o número de anos para pagar: "))
prestacao = valor_casa / (anos_para_pagar * 12)
if prestacao > (salario_comprador * 0.30):
    print("Empréstimo negado")
else:
    print("Empréstimo aprovado")
