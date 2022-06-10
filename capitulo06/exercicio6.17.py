estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2000, 1.20],
    "feijão": [100, 1.50]
}
total = 0
print("Vendas:\n")
while True:
    produto = input("Digite o nome do produto, fim para terminar: ")
    if produto == "fim":
        break
    if produto in estoque:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preço:5.2f} = {custo:5.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade insuficiente")
    else:
        print("Produto não encontrado")
print(f"\nTotal: {total:5.2f}")
print("\nEstoque:\n")
for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")