""" while True:
    v = int(input('Digite um valor entre 0 e 5: '))
    if v < 0 or v > 5:
        print('Valor inválido')
    else:
        break
print('Valor válido') """


def faixa_int(pergunta, minimo, maximo):
    while True:
        n = int(input(pergunta))
        if n < minimo or n > maximo:
            print(f"Valor inválido. Deve ser entre {minimo} e {maximo}")
        else:
            return n


print(faixa_int("Digite um número entre 0 e 5: ", 0, 5))
