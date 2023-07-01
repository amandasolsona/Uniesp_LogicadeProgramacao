#Se colocar a letra "A" o arquivo será adicionado abaixo;
#Se colocar a letra "W" se o arquivo não existir irá ser criado um novo arquivo txt e se o arquivo existir ele irá subscrever;
#\n é pra pular para próxima linha o texto;

with open('meu_arquivo.txt', 'w', encoding='utf-8') as fo:
    fo.write('Eu amo programar !\n')
    fo.write('Programar em SQL é muito bom !\n')
    fo.write('Java sempre foi pesado !\n')