with open("impares.txt", "w") as impares, open("pares.txt", "w") as pares:
    for i in range(1, 101):
        if i % 2 == 0:
            pares.write(f"{i}\n")
        else:
            impares.write(f"{i}\n")
