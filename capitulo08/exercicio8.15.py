L = [1, [2, 3, 4, [5, 6, 7]]]
ESPAÇOS_POR_NIVEL = 4


def imprime(l, nivel=0):
    espacos = " " * ESPAÇOS_POR_NIVEL * nivel
    if type(l) == list:
        print(espacos, "[")
        for i in l:
            imprime(i, nivel + 1)
        print(espacos, "]")
    else:
        print(espacos, l)


imprime(L)
