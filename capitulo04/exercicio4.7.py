categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    preço = 10
else:
    if categoria == 2:
        preço = 18
    else:
        if categoria == 3:
            preço = 23
        else:
            if categoria == 4:
                preço = 26
            else:
                if categoria == 5:
                    preço = 31
                else:
                    print("Categoria inválida, digite um valor de 1 a 5")
                    preço = 0
print(f"O preço do produto é de R$ {preço:.2f}")