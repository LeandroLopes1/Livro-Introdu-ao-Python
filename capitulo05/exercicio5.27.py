n_palindromo = int(input("Digite um número para verificar palindromo: "))
n_palindromo_invertido = 0
n_palindromo_invertido_aux = n_palindromo
while n_palindromo_invertido_aux > 0:
    n_palindromo_invertido = n_palindromo_invertido * 10 + n_palindromo_invertido_aux % 10
    n_palindromo_invertido_aux = n_palindromo_invertido_aux // 10
if n_palindromo == n_palindromo_invertido:
    print("É palindromo")
else:
    print("Não é palindromo")

