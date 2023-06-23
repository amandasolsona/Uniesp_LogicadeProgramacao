#[FORBELLONE, 2022] Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética desejada;
# calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual operação aritmética escolhida.

print('Calculadora')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operacao = input(f'Digite a operação (+, -, *, /, **): ')

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
elif operacao == '**':
    resultado = num1 ** num2
else:
    print('Operação inválida')
    resultado = None

if resultado is not None:

    print(f'O resultado é: {resultado}')
