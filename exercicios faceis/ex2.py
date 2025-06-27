'''
Solicite ao usuário 5 nomes e armazene em uma lista. Depois, imprima cada nome em uma linha.
'''

def nomes_por_linha():
    nomes = []

    for i in range(5):
        nome = input(f'Digite o {i+1}º nome: ')
        nomes.append(nome)

    for nome in nomes:
        print(nome)

nomes_por_linha()