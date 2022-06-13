String = 'TTAAC'

contador = {}
for letra in String:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

for chave, valor in contador.items():
    print(f"{chave}: {valor}x")
