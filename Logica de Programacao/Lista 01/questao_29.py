import math

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A distância entre os pontos P e Q é: {distancia:.2f}")