antes = [1, 2, 5, 6, 9]
depois = [1, 2, 8, 10]

conjunto_antes = set(antes)
conjunto_depois = set(depois)

print("Antes:", antes)
print("Depois:", depois)

print("Elementos que não mudaram:", conjunto_antes & conjunto_depois)
print("Os novos elementos:", conjunto_depois - conjunto_antes)
print("Os elementos que sairam:", conjunto_antes - conjunto_depois)