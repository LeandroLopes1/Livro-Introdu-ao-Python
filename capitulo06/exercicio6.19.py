lista_01 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
lista_02 = set([3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

lista_03 = lista_01 & lista_02
print("Valore comuns as duas lista:", lista_03)
lista_04 = lista_01 - lista_02
print("Valores que só existem na primeira lista:",lista_04)
lista_05 = lista_02 - lista_01
print("Valores que só existem na segunda lista",lista_05)
lista_06 = lista_01 ^ lista_02 
print("Elementos não repetidos nas duas listas", lista_06)
lista_07 = lista_01 - lista_02 
print("Primeira lista sem os valores repetidos na segunda",lista_07)