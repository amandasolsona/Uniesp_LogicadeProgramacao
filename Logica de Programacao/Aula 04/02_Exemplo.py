diretorio = 'teste\\'
arquivo = 'arquivo2.txt'
filepath = diretorio + arquivo


with open('teste\\arquivo2.txt', 'r', encoding='utf-8') as file_object:
    conteudo = file_object.read()
    print(conteudo)
