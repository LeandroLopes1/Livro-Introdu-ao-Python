estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2000, 1.20],
    "feijão": [100, 1.50]
}
venda =[["tomate", 20], ["batata", 1900], ["alface", 400], ["feijão", 50]]
total = 0
print("Vendas:\n")
for operação in venda:
    produto, quantidade = operação
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preço:5.2f} = {custo:5.2f}")
    total += custo
print(f"\nTotal: {total:5.2f}")
print("\nEstoque:\n")
for produto, (quantidade, preço) in estoque.items():
    quantidade = quantidade - sum(operação[1] for operação in venda if operação[0] == produto)
    print(f"{produto:12s}: {quantidade:3d}")
   