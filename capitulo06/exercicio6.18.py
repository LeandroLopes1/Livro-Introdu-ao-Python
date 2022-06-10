frase = input("Digite uma frase para contar as letras:")
d ={}
for letra in frase:
    if letra.isalpha():
        if letra in d:
            d[letra] += 1
        else:
            d[letra] = 1
print(d)