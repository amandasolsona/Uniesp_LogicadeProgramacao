#Nossa equipe de desenvolvimento ficou responsável por desenvolver um programa que gerencie uma lista de convidados
# para uma festa. É preciso criar uma mensagem padrão, e uma lista de convidados. Você pode escolher três personagens
# de filmes para adicionar a sua lista de convidados.
#Sabendo que um dos seus convidados não pode participar, adicione ao programa uma mensagem informando que ele será
# retirado da lista, e altere o código para receber um novo personagem. Não esqueça de utilizar as funções que te permite
# adicionar os novos convidados pelo teclado.
#Adicione a opção de poder adicionar mais pessoas à sua lista.
#Uma opção para adicionar um convidado querido ao início da lista;
#Uma convidado no meio da lista;
#E por um convidado ao fim da lista;


convidados = ['Thor', 'Hulk', 'Homem de Ferro']
mensagem = 'Você está convidado para minha festa!'

for convidado in convidados:
    print(f"{convidado}, {mensagem}")

print(f"\nInfelizmente, {convidados[0]} não poderá comparecer à festa.\n")

convidados[1] = input("Digite o nome do novo convidado: ")

for convidado in convidados:
    print(f"{convidado}, {mensagem}")

while True:
    adicionar_mais = input("\nGostaria de adicionar mais convidados? (s/n): ")
    if adicionar_mais.lower() == 'n':
        break
    posicao = input("Onde gostaria de adicionar o novo convidado? (inicio/meio/fim): ")
    novo_convidado = input("Digite o nome do novo convidado: ")
    if posicao.lower() == 'inicio':
        convidados.insert(0, novo_convidado)
    elif posicao.lower() == 'meio':
        convidados.insert(len(convidados)//2, novo_convidado)
    elif posicao.lower() == 'fim':
        convidados.append(novo_convidado)

print("\nLista final de convidados:")
for convidado in convidados:
    print(f"{convidado}, {mensagem}")