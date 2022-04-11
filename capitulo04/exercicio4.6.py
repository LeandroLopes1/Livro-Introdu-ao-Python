distancia_em_km = float(input("Digite a distância em km: "))
if distancia_em_km <= 200:
    valor_passagem = distancia_em_km * 0.50
    print(f"O valor da passagem é de R$ {valor_passagem:.2f}")
else:
    valor_passagem = distancia_em_km * 0.45
    print(f"O valor da passagem é de R$ {valor_passagem:.2f}")