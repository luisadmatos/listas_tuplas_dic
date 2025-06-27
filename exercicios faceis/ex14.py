'''
 Crie uma lista com 3 frutas e adicione uma quarta no in´ ıcio com insert.
'''

def lista_frutas():

    frutas = ['Banana', 'Maça', 'Morango']
    frutas.insert(0, 'Uva')
    return frutas

print(lista_frutas())