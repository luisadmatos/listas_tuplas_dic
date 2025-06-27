'''
 Leia 5 n´ umeros do usu´ ario e verifique se cada um deles ´ e maior que 10.
'''
def numeros_usuario():

    for i in range(1,6):
        input(f'Digite o {i}º número: ')

        if i > 10:
            print(f'Número {i} é maior que 10')
        else: 
            print(f'Número {i} é menor que 10')

numeros_usuario()
