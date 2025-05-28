
notas = {
    'Ana': [10.0, 5.0, 8.0],
    'Vitor': [8.0, 2.5, 9.7],
    'Rafael': [10.0, 9.5, 8.3],
    'Lucas': [7.0, 10.0, 8.7]
}

for aluno, nota in notas.items():
    media = sum(nota) / len(nota)
    print(f'A media do aluno {aluno} é: {media: .2f}')