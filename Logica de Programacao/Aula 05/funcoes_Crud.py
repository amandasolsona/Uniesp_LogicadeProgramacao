def cadastrar(lista):
    nome_pessoa = input('Digite o nome da pessoa: ')
    lista.append(nome_pessoa)
    return lista


def listar(lista):

    for nome in lista:
        print(f'-> {nome}')

def remover(lista):

    nome_remover = input('Digite qual aluno será removido: ')

    if nome_remover in lista:
        lista.remove(nome_remover)
    else:
        print('Nome não encontrados!')

    return lista

def editar(lista):
    nome_editar = input('Digite o nome a ser alterado: ')

    if nome_editar in lista:
        print(f'O nome {nome_editar} foi encontrado.')
        alteracao = input('Qual será o novo nome? ')
        lista[lista.index(nome_editar)] = alteracao

    else:
        print('O nome não foi encontrado!')

    return lista

def salvar_arquivo(lista):
    with open('nomes_alunos.txt', 'w', encoding='utf-8') as file_object:
        # file_object.writelines(i + '\n' for i in lista) ou
        for i in lista:
            file_object.write((i + '\n'))

def ler_arquivo():
    with open('nomes_alunos.txt', 'r', encoding='utf-8') as file_object:
        lista_bd = file_object.readlines()
        lista = []

        for i in lista_bd:
            lista.append(i.rstrip())

        return lista