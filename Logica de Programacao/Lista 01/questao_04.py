#Exercício do Desconto: Escreva um programa em Python que solicite ao usuário o valor de um produto e o
# percentual de desconto. Calcule o valor do desconto e exiba o valor final após o desconto.

preco_original = float(input("Qual é o valor original: R$ "))

desconto = float(input("Qual o Desconto (em %) para esse produto: "))

desconto = desconto / 100

print(f'Valor original:     R$', preco_original)
print(f'Desconto ganho:     R$', preco_original * desconto)
print(f'Valor com desconto: R$', preco_original * (1-desconto))