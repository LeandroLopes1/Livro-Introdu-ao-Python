import string


string_01 = "AATTGGAA"
string_02 = "TG"

caracters_apenas_string_01 = []
for caracter in string_01:
    if caracter not in string_02:
        caracters_apenas_string_01.append(caracter)

print('Caracteres apenas na primeira string: ', ''.join(caracters_apenas_string_01))