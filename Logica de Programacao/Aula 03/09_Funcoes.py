import minhas_funcoes
from random import randint

condicao = True

while condicao:
    op = input('Digite a opção: \n'
               '1 - Somar\n'
               '2 - Subtrair\n'
               '3 - Sair')
    op = int(op)

    match op:
        case 1:
            resultado = minhas_funcoes.somar(
                randint(1, 5),
                randint(1, 5))
            print(f'A soma foi: {resultado}')
        case 2:
            resultado = minhas_funcoes.subtrair(
                randint(100, 200),
                randint(100, 200))
            print(f'A subtração foi: {resultado}')
        case 3:
            condicao = False
        case _:
            print(f'Opção inválida!')