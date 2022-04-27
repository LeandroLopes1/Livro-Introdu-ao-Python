n = float(input("Digite um número para encontrar sua raiz quadrada: "))
b = 2
while abs(n - b**2) > 0.00001:
    b = (n/b + b)/2
print(f"A raiz quadrada de {n} é {b:.4f}")