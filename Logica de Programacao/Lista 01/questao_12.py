#Um programa é necessário para habilitar o funcionamento de uma conta corrente em um banco digital.
#O programa deve permitir ao cliente iniciar com um depósito, realizar um saque, e ao final verificar se o saldo da
#conta está positivo ou negativo. Se negativo, informa qual o valor será necessário para quitar o débito.

deposito = float(input('Deposite o valor:'))
saque = float(input('Digite o valor para saque:'))

saldo = deposito - saque

if saldo >= 0:
    print(f"Seu saldo é positivo: R${saldo:.2f}")
else:
    print(f"Seu saldo é negativo: R${saldo:.2f}")
    print(f"Você precisa depositar R${abs(saldo):.2f} para quitar o débito.")
