quantidade_dias = int(input("Digite a quantidade de dias: "))
quantidade_horas = int(input("Digite a quantidade de horas: "))
quantidade_minutos = int(input("Digite a quantidade de minutos: "))
quantidade_segundos = int(input("Digite a quantidade de segundos: "))
total_em_segundos = (quantidade_dias * 24 * 60 * 60) + (quantidade_horas * 60 * 60) + (quantidade_minutos * 60) + quantidade_segundos
print(f"O total em segundos é: {total_em_segundos}")