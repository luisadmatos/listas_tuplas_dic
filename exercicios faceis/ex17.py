'''
Crie uma lista com 5 números e calcule a média usando laço for.
'''
def media():

    lista = [2, 4, 6, 8, 10]

    media = sum(lista) / len(lista)

    return media

print(media())