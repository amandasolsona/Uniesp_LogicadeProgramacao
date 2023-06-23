#Exercício da Conversão de Moedas: Escreva um programa em Python que solicite ao usuário um valor em Real (BRL)
#e faça a conversão desse valor para Dólar Americano (USD). Considere a taxa de câmbio fixa de 1 USD = 5 BRL.
#Exiba o valor convertido na tela.

real = float(input('Qual o valor em real (R$) que deseja realizar a conversão? '))
dolar = real/5

print(f'O valor em dólar (USD) é {dolar:0.2f}')