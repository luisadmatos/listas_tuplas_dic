
palavras = ['oi', 'musica', 'nao', 'ok', 'otorrinolaringologista']
menores_que_tres = []

for palavra in palavras:
    if len(palavra) < 3:
        palavras.remove(palavra)
print(palavras)