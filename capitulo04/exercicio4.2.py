velocidade_carro = float(input("Digite a velocidade do carro: "))
if velocidade_carro > 80:
    print("Você foi multado!")
    multa = (velocidade_carro - 80) * 5
    print("O valor da multa é de R$ %.2f" % multa)
else:
    print("Você está dentro do limite de velocidade!")