
nomes_idades = [('ana', 20), ('luisa', 21), ('vitor', 27)]

maior_idade = max(nomes_idades, key=lambda pessoa: pessoa[1])
menor_idade = min(nomes_idades, key=lambda pessoa: pessoa[1])

print(maior_idade)
print(menor_idade)