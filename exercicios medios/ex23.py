
nomes = ['laura', 'laura', 'livia', 'helena', 'helena', 'lorenzo', 'lorenzo', 'benicio']

nao_duplicados = set()
ordem_correta = []

for nome in nomes:
    if nome not in nao_duplicados:
        nao_duplicados.add(nome)
        ordem_correta.append(nome)
    
print(ordem_correta)