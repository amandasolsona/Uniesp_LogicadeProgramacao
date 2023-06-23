#Escreva um programa em Python que peça ao usuário para digitar a temperatura
# em graus Celsius e converta-a para Fahrenheit. A
# fórmula de conversão é: Fahrenheit = (Celsius * 9/5) + 32.

#Temperatura
celsius = float(input('Digite a temperatura em graus celsius: '))
fahrenheit = (celsius * 9/5) + 32

print(f'A temperatura em fahrenheit é {fahrenheit}')