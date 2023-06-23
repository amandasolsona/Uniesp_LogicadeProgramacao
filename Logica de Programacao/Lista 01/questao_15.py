#[FORBELLONE, 2022] O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saúde para indicar
#a condição de peso de uma pessoa. A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a
#altura de um adulto e mostre sua condição.

peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso / (altura*altura)

if imc < 18.5:
    print(f'Você encontra-se abaixo do peso, conforme seu imc {imc:0.2f}')
elif 18.5 <= imc <= 25:
    print(f'Você encontra-se com peso normal, conforme seu imc {imc:0.2f}')
elif 25 <= imc <= 30:
    print(f'Você encontra-se acima do peso, conforme seu imc {imc:0.2f}')
else:
    print(f'Você encontra-se obeso, conforme seu imc {imc:0.2f}')