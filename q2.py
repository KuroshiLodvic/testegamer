alfabeto = {
    '61': 'a', '67': 'g', '6c': 'l', '71': 'q', '76': 'v',
    '62': 'b', '68': 'h', '6d': 'm', '72': 'r', '77': 'w',
    '63': 'c', '69': 'i', '6e': 'n', '73': 's', '78': 'x',
    '64': 'd', '6a': 'j', '6f': 'o', '74': 't', '79': 'y',
    '65': 'e', '6b': 'k', '70': 'p', '75': 'u', '7a': 'z',
    '66': 'f', '20': ' '
}

def decodificador(entrada:list) -> str:
    texto_final = ''
    
    for codigo in entrada:
        for letra in alfabeto:
            if codigo == letra:
                texto_final += alfabeto[codigo]

    return print(texto_final)

decodificador(['65','75','20','61','6d','6f','20','70','72','6f','67','72','61','6d','61','72'])