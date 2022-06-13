string_01 = 'CTA'
string_02 = 'ABC'

caracteres_incomuns = []
for caracter in string_01:
    if caracter not in string_02:
        caracteres_incomuns.append(caracter)

for caracter in string_02:
    if caracter not in string_01:
        caracteres_incomuns.append(caracter)       

print('Caracteres incomuns: ', ''.join(caracteres_incomuns))
