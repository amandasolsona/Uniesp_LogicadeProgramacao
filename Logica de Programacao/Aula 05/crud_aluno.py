import funcoes_Crud
from datetime import datetime

lista_nomes = funcoes_Crud.ler_arquivo()

while True:

    print('1 - Cadastrar aluno(a)\n'
          '2 - Remover aluno(a)\n'
          '3 - Editar aluno(a)\n'
          '4 - Listar alunos\n'
          '0 - Sair')

    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            lista_nomes = funcoes_Crud.cadastrar(lista=lista_nomes)
            print(f'{datetime.now()} - Aluno cadastrado com sucesso ! ')

        case 2:
            lista_nomes = funcoes_Crud.remover(lista=lista_nomes)
            print(f'{datetime.now()} - Aluno removido com sucesso ! ')

        case 3:
            lista_nomes = funcoes_Crud.editar(lista=lista_nomes)
            print(f'{datetime.now()} - Aluno alterado com sucesso ! ')

        case 4:
            funcoes_Crud.listar(lista=lista_nomes)
            print(f'{datetime.now()} - Lista de alunos gerada com sucesso ! ')


        case 0:
            print(f'Programa finalizado...')
            break