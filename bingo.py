cartela = {
    'B': [6, 23, 31, 55, 65],
    'I': [5, 19, 34, 50, 63],
    'N': [8, 29, 60, 48, 68],
    'G': [15, 30, 39, 49, 67],
    'O': [9, 28, 40, 47, 75]
}

entrada = [41, 6, 12, 58, 31, 68, 2, 19, 23, 45, 62, 55, 3, 38, 51, 65, 27, 15, 49, 8]

for coluna in cartela:
    cont = 0
    for num in entrada:
        if num in cartela[coluna]:
            cont += 1
    if cont == len(cartela[coluna]):
        print(f'A coluna {coluna} foi vencedora!')
        break