def validar_string(palavra, maximo, minimo):
    while True:
        n = input(palavra)
        if len(n) > maximo or len(n) < minimo:
            print(f"Valor inválido. Deve ter {minimo} e {maximo} caracteres")
        else:
            return n
print(validar_string("Digite uma string de até 5 caracteres: ", 5, 1))
    