temperatura = [-10, -8, 0, 1, 2, 5, -2, -4]
minimo = temperatura[0]
maximo = temperatura[0]
media = 0
for i in temperatura:
    if i < minimo:
        minimo = i
    if i > maximo:
        maximo = i
    media += i
media = media / len(temperatura)
print(f"O menor valor da lista é {minimo}")
print(f"O maior valor da lista é {maximo}")
print(f"A média dos valores da lista é {media}")
