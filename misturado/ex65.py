'''
 Faça um programa que recebe nomes de alunos e suas idades. Armazene usando
 uma lista de tuplas e depois transforme em dicionário.
'''
dados = []

def dados_alunos():

    n = int(input('Digite a quantidade de alunos que deseja cadastrar: '))

    for _ in range(n):
        nome = input('Digite o nome do aluno: ')
        idade = input('Digite a idade do aluno: ')
        dados.append((nome, idade))

dados_alunos()
print(dados)