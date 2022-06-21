def valida_entrada(mensagem, opçoes_validas):
    opçoes = opçoes_validas.lower()
    while True:
        entrada = input(mensagem)
        if entrada.lower() in opçoes:
            break
        else:
            print(f"Opção inválida. Digite uma opção válida: {opçoes_validas}")
    return entrada

print(valida_entrada("Digite uma opção: ", "abcde"))