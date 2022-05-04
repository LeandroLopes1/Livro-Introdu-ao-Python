L = [5, 7, 2, 4]
minimo = L[0]
for i in L:
    if i < minimo:
        minimo = i
print(f"O menor valor da lista é {minimo}")