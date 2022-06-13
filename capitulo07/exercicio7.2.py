string_01 = 'AAACTBF'
string_02 = 'CBT'

caracteres_comuns = []
for caracter in string_01:
    if caracter in string_02:
        caracteres_comuns.append(caracter)


s = ''.join(caracteres_comuns)
print(s)
