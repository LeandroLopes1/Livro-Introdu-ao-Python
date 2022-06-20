def palavra_dentro_da_lista(lista, palavra):
    if palavra in lista:
        return True
    return False

print(palavra_dentro_da_lista(["a", "b", "c"], "b"))