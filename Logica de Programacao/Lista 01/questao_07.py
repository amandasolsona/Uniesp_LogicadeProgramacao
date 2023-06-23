#Exercício do Tempo de Viagem: Escreva um programa em Python que solicite ao usuário a distância de uma viagem (em km)
#e a velocidade média (em km/h). Calcule o tempo de viagem em horas e exiba o resultado.

distancia = float(input('Qual a distância (em KM): '))
velocidade = float(input('Qual a velocidade média (em KM/H:'))
tempo_viagem = distancia/velocidade


print(f'O tempo estimando da viagem foi de {tempo_viagem:0.2f} horas ')



