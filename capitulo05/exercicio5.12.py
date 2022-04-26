deposito_inicial = float(input("Digite o valor do deposito inicial: "))
taxa_juros = float(input("Digite a taxa de juros: "))
deposito_mensal = float(input("Digite o valor do deposito mensal: "))

mes = 1
valor_mensal = deposito_inicial

while mes <= 24:
    valor_mensal = valor_mensal + deposito_mensal + (valor_mensal * (taxa_juros / 100))
    mes = mes + 1

    print(f"O valor da conta no mes {mes} é R$ {valor_mensal:.2f}")
print(f"O valor total da conta é R${valor_mensal:.2f}")
print(f"O ganho obtido com a taxa de juros de {taxa_juros}% é R${valor_mensal - deposito_inicial:.2f}")
