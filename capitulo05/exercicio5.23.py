numero_primo = int(input("Insira o número para verificar se é primo: "))
numero_divisor = 2
if numero_primo == 1 or numero_primo == 0:
    print("Não é primo")
else:
    while numero_divisor < numero_primo:
        if numero_primo % numero_divisor == 0:
            print("Não é primo")
            break
        else:
            numero_divisor += 1
    else:
        print("É primo")

