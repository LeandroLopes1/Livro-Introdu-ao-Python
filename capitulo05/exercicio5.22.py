insira_operação = input("Insira a operação (+, -, / , *, s de sair): ")
tabuada = int(input("Insira o número da tabuada: "))
while  tabuada <= 10:
    numero = 1
    while numero <= 10:
        if insira_operação == "+":
            print(f"{tabuada} + {numero} = {tabuada + numero}")
        elif insira_operação == "-":
            print(f"{tabuada} - {numero} = {tabuada - numero}")
        elif insira_operação == "*":
            print(f"{tabuada} * {numero} = {tabuada * numero}")
        elif insira_operação == "/":
            print(f"{tabuada} / {numero} = {tabuada / numero}")
        numero += 1
  
    if insira_operação == "s":
        break
    else:
        insira_operação = input("Insira a operação (+, -, / , *, s de sair): ")
        if insira_operação == "s":
            break
        tabuada = int(input("Insira o número da tabuada: "))       
print("Fim")