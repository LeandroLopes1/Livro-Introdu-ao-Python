preço_mercadoria = float(input("Digite o preço da marcadoria: "))
desconto = float(input("Digite o desconto: "))
preço_final = preço_mercadoria - (preço_mercadoria * desconto / 100)    
print(f"O valor do desconto é: {preço_mercadoria * desconto / 100:.2f}")
print(f"O preço final é de: {preço_final:.2f}")
