apagar = 0

while True:
    codigo_produto = int(input("Digite o código do produto (0 para sair): "))
    preço = 0
    if codigo_produto == 0:
        break
    elif codigo_produto == 1:
        preço = 0.50
    elif codigo_produto == 2:
        preço = 1.00
    elif codigo_produto == 3:
        preço = 4.00
    elif codigo_produto == 5:
        preço = 7.00
    elif codigo_produto == 9:
        preço = 8.00
    else:
        print("Código inválido")
    if preço != 0:
        quantidade = int(input("Digite a quantidade: "))
        apagar += preço * quantidade
print(f"O valor a pagar é R${apagar:.2f}")
