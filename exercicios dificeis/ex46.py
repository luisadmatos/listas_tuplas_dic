
lista = [5, 4, 1, 2, 3]

for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)


# bubble sort: maneira de ordenar elementos de uma lista
# cuidado: esquema bubble sort pode ser ineficiente em listas mto grandes