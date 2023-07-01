#with open('arquivo.TXT', 'r', encoding='utf-8') as fo:
    #for linha in fo:
        #if 'C' in linha:
            #print(f'Tipo: {type(linha)} | {linha.rstrip()}')

print('-----Iniciando o Programa-----')

op = input('Digite 0 para quem não tem permissão e 1 para quem tem permissão: ')

with open('arquivo.TXT', 'r', encoding='utf-8') as fo:
    for linha in fo:
        if linha[0] == op:
            print(linha[2:].rstrip())

#0, 1, 2 - Refere-se a ordem dos caracteres no arquivo