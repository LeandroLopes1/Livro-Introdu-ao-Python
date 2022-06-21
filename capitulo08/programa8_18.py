def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= minimo and v <= maximo:
                return v
            else:
                print(f"Valor inválido. Deve ter {minimo} e {maximo} caracteres")
        except ValueError:
            print("Valor inválido. Deve ser um número inteiro")

