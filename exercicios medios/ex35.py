
nome_idade = [('Luisa', 20), ('Bruno', 27), ('Vinicius', 19), ('Emily', 18), ('Lucas', 19), ('Leonardo', 18)]

for nome, idade in nome_idade:
    if idade > 18:
        print(f'As pessoas com mais de 18 anos são: {nome}')