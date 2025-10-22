def verificar_vencedor(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]:
            return print(f'O jogador {tabuleiro[i][0]} ganhou!')
        
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j]:
            return print(f'O jogador {tabuleiro[0][j]} ganhou!')
        
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return print(f'O jogador {tabuleiro[0][0]} ganhou!')
    
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return print(f'O jogador {tabuleiro[1][1]} ganhou!')
    
    return print('Empate')

tabuleiro_vitoria_X = [
    ['X', 'O', 'O'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X']
]

tabuleiro_vitoria_O = [
    ['X', 'X', 'O'],
    ['O', 'O', 'O'],
    ['X', 'O', 'X']
]

tabuleiro_empate = [
    ['X', 'O', 'X'],
    ['X', 'O', 'O'],
    ['O', 'X', 'X']
]

verificar_vencedor(tabuleiro_vitoria_X)
verificar_vencedor(tabuleiro_vitoria_O)
verificar_vencedor(tabuleiro_empate)