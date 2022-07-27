import sys

if len(sys.argv) != 2:
    print("\nUso: exercicio9_1.py <nome_arquivo>\n")
else:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
    for linha in arquivo.readlines():
        print(linha[:-1])
    arquivo.close()
