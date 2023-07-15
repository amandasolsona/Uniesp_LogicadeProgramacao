# Escreva um programa que contenha uma função chamada soma_dois_inteiros, essa função
# será responsável por somar dois números inteiros (somente inteiros).
# • Nessa função faça um tratamento de exceção para o
# caso do usuário digitar números que não sejam inteiros.

try:
    numero1 = int(input("Digite o primeiro número:"))
    numero2 = int(input("Digite o segundo número:"))

    resultado = numero1 + numero2
    print("O resultado da soma é: ", resultado)

except ValueError:
    print("Digite apenas números inteiros.")


