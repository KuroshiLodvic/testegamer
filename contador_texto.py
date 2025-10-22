texto = 'Muitos editores de texto possuem a função de contar a ocorrência de cada palavra no texto. Faça um programa que recebe um texto e conta a ocorrência de cada palavra no texto, retornando um dicionário com as palavras e suas respectivas contagens.'
palavras = {}

def contador_texto(texto:str) -> dict:
    novo_texto = texto.split()
    
    for palavra_base in novo_texto:
        cont = 0

        for palavra_buscada in novo_texto:
            if palavra_base == palavra_buscada:
                cont += 1

        palavras[palavra_base] = cont

    return palavras

print(contador_texto(texto))