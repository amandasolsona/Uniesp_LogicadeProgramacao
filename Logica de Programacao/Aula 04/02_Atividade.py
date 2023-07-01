import projeto_Funcoes

lista_nomes = projeto_Funcoes.ler_arquivo()

while True:

    print('1 - Adicionar\n'
          '2 - Pesquisar\n'
          '3 - Listar\n'
          '4 - Remover\n'
          '5 - Alterar\n'
          '6 - Salvar em arquivo\n'
          '7 - Recuperar arquivo\n'
          '0 - Sair')

    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            lista_nomes = projeto_Funcoes.adicionar(lista=lista_nomes)

        case 2:
            projeto_Funcoes.pesquisar(lista=lista_nomes)

        case 3:
            projeto_Funcoes.listar(lista=lista_nomes)

        case 4:
            lista_nomes = projeto_Funcoes.remover(lista=lista_nomes)

        case 5:
            lista_nomes = projeto_Funcoes.alterar(lista=lista_nomes)

        case 6:
           projeto_Funcoes.salvar_arquivo(lista=lista_nomes)

        case 7:
            lista_nomes = projeto_Funcoes.ler_arquivo()

        case 0:
            print(f'Programa finalizando...')
            break

