valor_inicial_divida = float(input("Digite o valor da dívida: "))
taxa_juros = float(input("Digite a taxa de juros: "))
valor_mensal_pago = float(input("Digite o valor mensal pago: "))

mes = 1

if (valor_inicial_divida * taxa_juros / 100) > valor_mensal_pago:
    print("Não foi possível pagar a dívida.")
else:
    valor_mensal = valor_inicial_divida
    juros_pagos = 0

    while valor_mensal > valor_mensal_pago:
        juros = valor_mensal * (taxa_juros / 100)
        valor_mensal = valor_mensal + juros - valor_mensal_pago
        juros_pagos = juros_pagos + juros
        print(f"O valor da dívida no mes {mes} é R$ {valor_mensal:.2f}")
        mes = mes + 1
    print(f"Para pagar a dívida de R${valor_inicial_divida:.2f} com juros de {taxa_juros},")
    print(f"voce precisara de {mes - 1} meses, e pagará R${juros_pagos:.2f} de juros.")
    print(f"No ultimo mes, voce teria um saldo residual de R$ {valor_mensal:.2f} a pagar")
