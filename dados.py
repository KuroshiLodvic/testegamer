dados = [
    ("João", "TI"),
    ("Maria", "RH"),
    ("Pedro", "TI"),
    ("Ana", "Financeiro"),
    ("Clara", "RH")
]

dicionario = {}

for func, setor in dados:
    if setor in dicionario:
        dicionario[setor].append(func)
    else:
        dicionario[setor] = [func]

print(dicionario)