cigarros_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Quantos anos você fuma? "))
dias_perdidos = anos_fumando * 365 * cigarros_dia * 10 / 1440
print("Você perdeu %d dias de vida" % dias_perdidos)