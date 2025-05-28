
lista_listas = [[11, 12], [13, 14], [15, 16], [17, 18]]
flattened = []

for sublista in lista_listas:
    for item in sublista:
        flattened.append(item)

print(flattened)