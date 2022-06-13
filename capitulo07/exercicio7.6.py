string_01 = 'AATTCGAA'
string_02 = 'TG'
string_03 = 'AC'

subtitui_string_02_por_string_03 = []
for caracter in string_01:
   posiçao = string_02.find(caracter)
   if posiçao != -1:
        subtitui_string_02_por_string_03.append(string_03[posiçao])
   else:
        subtitui_string_02_por_string_03.append(caracter)

print('String 01 substituida por string 02: ', ''.join(subtitui_string_02_por_string_03))
    