with open('arquivo.TXT', 'r', encoding='utf-8') as file_object:
    conteudo = file_object.read()
    print(conteudo)
    print(f'Tipo: {type (conteudo)} \n{conteudo}')