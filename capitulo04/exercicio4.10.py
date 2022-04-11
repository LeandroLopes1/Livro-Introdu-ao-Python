quantidade_kWh = float(input("Digite a quantidade de kWh gasta: "))
tipo_de_instalação = input("Digite o tipo de instalação (R, I, C): ")
if tipo_de_instalação == "R":
    if quantidade_kWh <= 500:
        valor_a_pagar = quantidade_kWh * 0.40
    else:
        valor_a_pagar = quantidade_kWh * 0.65
elif tipo_de_instalação == "I":
    if quantidade_kWh <= 5000:
        valor_a_pagar = quantidade_kWh * 0.55
    else:
        valor_a_pagar = quantidade_kWh * 0.60
elif tipo_de_instalação == "C":
    if quantidade_kWh <= 1000:
        valor_a_pagar = quantidade_kWh * 0.55
    else:
        valor_a_pagar = quantidade_kWh * 0.60
print(f"O valor a pagar é de R$ {valor_a_pagar:.2f}")
