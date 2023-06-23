#Gerenciar um estoque para a empresa U não é complicado, mas ele te pediu para desenvolver um programa para
# realizar esta tarefa. Ela precisa que o usuário informe a quantidade máxima e mínima do estoque do produto X,
# e também a quantidade real existente no estoque. Por fim, o programa deve responder se é necessário adquirir
# mais produtos, comparando o estoque real com a média entre valor máximo e mínimo.
#se o estoque real estiver abaixo da média, informar a necessidade de compra;
#se estiver acima da média informar que não precisa adquirir novos produtos;
#se estiver na média, informa que em breve será necessária nova aquisição de produtos;

estoque_maximo = float(input('Digite o valor máximo do estoque do produto x:'))
estoque_minimo = float(input('Digite o valor mínimo do estoque do produto x:'))
estoque_real = float(input('Digite a quantidade real do estoque:'))
estoque_media = (estoque_maximo+estoque_minimo)/2


if estoque_real < estoque_media:
    print(f"Seu estoque encontra-se abaixo da média, por gentileza comprar novos produtos")
elif estoque_real > estoque_media:
    print(f"Seu estoque encontra-se acima da média, não precisa adquirir novos produtos")
else:
    print(f"Em breve será necessária nova aquisição de produtos.")


