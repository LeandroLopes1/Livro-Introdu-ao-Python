import sys

if len(sys.argv) != 4:
    print("\nUso: python3 exercicio9_4.py <nome_arquivo>"
          "<nome_arquivo_meio> <nome_arquivo_saida>\n\n")
else:
    nome_arquivo = sys.argv[1]
    nome_arquivo_meio = sys.argv[2]
    nome_arquivo_saida = sys.argv[3]
    arquivo_entrada = open(nome_arquivo, "r")
    arquivo_meio = open(nome_arquivo_meio, "r")
    arquivo_saida = open(nome_arquivo_saida, "w")
    for linha in arquivo_entrada.readlines():
        arquivo_saida.write(linha)
    for linha in arquivo_meio.readlines():
        arquivo_saida.write(linha)
    arquivo_entrada.close()
    arquivo_meio.close()
    arquivo_saida.close()
    print("Arquivo gerado com sucesso!")
