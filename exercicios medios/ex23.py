'''
 Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a
 ordem.
'''
nomes = ['laura', 'laura', 'livia', 'helena', 'helena', 'lorenzo', 'lorenzo', 'benicio']

def eliminar_duplicados(nomes):
    nao_duplicados = set()
    ordem_correta = []

    for nome in nomes:
        if nome not in nao_duplicados:
            nao_duplicados.add(nome)
            ordem_correta.append(nome)
    
    return ordem_correta

print(eliminar_duplicados(nomes))