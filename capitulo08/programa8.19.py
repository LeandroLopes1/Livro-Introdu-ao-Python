from programa8_18 import valida_inteiro

L = []
for i in range(3):
    L.append(valida_inteiro("Digite um número: ", 0, 20))
print(f"Soma: {sum(L)}")
