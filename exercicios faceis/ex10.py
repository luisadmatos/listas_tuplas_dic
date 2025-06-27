'''
 Dada uma lista de palavras, junte todas elas em uma string separada por vírgulas.
'''
def juntar_palavras():
    palavras = ['chocolate', 'sorvete', 'goma', 'bala', 'brigadeiro'] 

    resultado = ', '.join(palavras)
    return resultado

print(juntar_palavras())