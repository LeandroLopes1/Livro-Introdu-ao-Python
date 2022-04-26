n = int(input("Tabuada de qual numero: "))
inicio = int(input("Digite um inicio da tabuada: "))
fim = int(input("Digite um ultimo numero a imprimir: "))
x = inicio
while x <= fim:
    print(n, "x", x, "=", n*x)
    x = x + 1