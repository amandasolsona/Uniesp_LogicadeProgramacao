#Exercício da Conversão de Temperatura: Escreva um programa em Python que solicite ao usuário uma temperatura em graus
#Celsius e faça a conversão para Fahrenheit. Exiba o resultado na tela.

celsius = float(input('Digite a temperatura para realização da conversão:'))
fahrenheit = (celsius * 1.8) + 32

print(f'A temperatura em celsius é {celsius}')
print(f'A temperatura em fahrenheit é {fahrenheit}')