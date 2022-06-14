# Jogo da velha

velha = """               Posições
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
"""

# Uma lista de posições (linha e coluna) para cada posição válida do jogo
# Um elemento extra foi adicionado para facilitar a manipulação
# dos índices e para que estes tenham o mesmo valor da posição
#
#  7 | 8 | 9
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  1 | 2 | 3

posições = [
    None,   # 0
    (5, 1), # 1
    (5, 5), # 2
    (5, 9), # 3
    (3, 1), # 4
    (3, 5), # 5
    (3, 9), # 6
    (1, 1), # 7
    (1, 5), # 8
    (1, 9), # 9
]

# Posições que levam ao ganho do jogo
# Jogadas fazendo uma linha, um coluna ou as diagonais ganham
# Os números representam as posições ganhadoras

ganho = [
    [1, 2, 3], # linha
    [4, 5, 6], # linha
    [7, 8, 9], # linha
    [1, 4, 7], # coluna
    [2, 5, 8], # coluna
    [3, 6, 9], # coluna
    [1, 5, 9], # diagonal
    [3, 5, 7], # diagonal
]

# Constroi o tabuleiro a partir das strings
# gerando uma lista de listas que pode ser modificada

tabuleiro = []
for linha in velha.splitlines():
    tabuleiro.append(list(linha))

jogador = "X" # Começa jogando com X
jogando = True
jogadas = 0 # Contador de jogadas - usado para saber se velhou
while True:
    for t in tabuleiro: # Imprime o tabuleiro
        print("".join(t))
    if not jogando: # Termina apos imprimir o último tabuleiro
        break
    if jogadas == 9: # Se 9 jogadas foram feitas, todos os espaços foram preenchidos
        print("Deu velha! Ninguém ganhou.")
        break
    jogada = int(input(f"Digite a posição a jogar 1-9 (jogador {jogador}):"))
    if jogada < 1 or jogada > 9: # Se a posição não estiver entre 1 e 9 mostra mensagem de erro
        print("Posição inválida")
        continue
    if tabuleiro[posições[jogada][0]][posições[jogada][1]] != " ": # Se a posição já estiver preenchida mostra mensagem de erro
        print("Posição já preenchida")
        continue
    tabuleiro[posições[jogada][0]][posições[jogada][1]] = jogador # Preenche a posição com o símbolo do jogador
    # Verifica se o jogador ganhou
    for p in ganho:
        for x in p:
            if tabuleiro[posições[x][0]][posições[x][1]] != jogador:
                break
        else:
            print(f"O jogador {jogador} ganhou ({p})")
            jogando = False
            break
    jogador = "X" if jogador == "O" else "O" # Alterna o jogador
    jogadas += 1 # Contador de jogadas

