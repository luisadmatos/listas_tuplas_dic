
alunos = []

for i in range(6):
    nome = input('Digite seu nome: ')
    nota = int(input('Digite sua nota: '))
    aluno = (nome, nota)
    alunos.append(aluno)

ordenados = sorted(alunos, key=lambda x: x[1], reverse=True)    
print(ordenados)