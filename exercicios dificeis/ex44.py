
itens = [11, 12, 13, 14, 15, 16, 17, 18]
divisao = 2
sublistas = []

for i in range(0, len(itens), divisao):
    processo = itens[i:i+divisao]
    sublistas.append(processo)

print(sublistas)