#Tratamento de Exceções
#Try - o código que pode gerar uma exceção;
#Except - código que é executado caso ocorra alguma exceção;
# ValueError: Se o usuário digitar algo que não seja um número inteiro
# ZeroDivisionError: Se o segundo número for zero.

#Calculadora

try:
    numero1 = int(input("Digite o primeiro número:"))
    numero2 = int(input("Digite o segundo número:"))

    resultado = numero1 / numero2
    print("O resultado da divisão é: ", resultado)

except ValueError:
    print("Digite apenas números inteiros.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")