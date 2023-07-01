#Desenvolva um programa em Python para:
#Imprimir todas as linhas dos livros em anexo;
#Contar quantas linhas cada livro apresenta.

with open('contos_dos_irmaos_grimm.txt', 'r', encoding='utf-8') as file_object:
    livro = file_object.read()
print(livro)

with open('contos_dos_irmaos_grimm.txt', 'r', encoding='utf-8') as file_object:
    linhas = file_object.readlines()

    contador = 0
    for linha in linhas:
        contador += 1
print(f'Número de linhas: {len(linhas)}')

with open('o_principe_maquiavel.txt', 'r', encoding='utf-8') as file_object:
    livro = file_object.read()
print(livro)

with open('o_principe_maquiavel.txt', 'r', encoding='utf-8') as file_object:
    linhas = file_object.readlines()

    contador = 0
    for linha in linhas:
        contador += 1
print(f'Número de linhas: {len(linhas)}')