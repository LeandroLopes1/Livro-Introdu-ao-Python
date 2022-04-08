km_percorrido = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias alugados: "))
valor_aluguel = km_percorrido * 0.15 + dias_alugados * 60
print("O valor do aluguel é R$ %.2f" % valor_aluguel)