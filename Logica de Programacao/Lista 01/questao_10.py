#Exercício do IMC (Índice de Massa Corporal): Escreva um programa em Python que solicite ao usuário sua altura em metros
# e seu peso em quilogramas. Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura * altura).
# Exiba o resultado do IMC na tela.


altura = float(input('Digite sua altura:'))
peso = float(input('Digite seu peso:'))
imc = peso / (altura*altura)


print(f'O valor do seu IMC é: {imc:.2f} ')