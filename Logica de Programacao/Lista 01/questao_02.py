#Desenvolva um programa para imprimir uma citação famosa. Pesquisa no Google uma citação
# famosa de uma pessoa ou personagem que você admire. Exiba a citação e o nome do autor. A saída do programa
# deverá ter a aparência a seguir, incluindo as aspas:
#Alvo Dumbledore: “Pode-se encontrar a felicidade mesmo nas horas mais sombrias se a pessoa lembrar de acender a luz”



frase = '\033[1mAlvo Dumbledore:''\033[0m\"\033[3mPode-se encontrar a ''felicidade mesmo nas horas mais sombrias se ''a essoas lembrar de acender a luz\033[0m\"'
print(frase)

#Este código imprime uma mensagem formatada com texto em negrito e itálico. Aqui está uma explicação detalhada:

# A variável mensagem é definida como uma string que contém várias sequências de escape ANSI para formatar o texto.
# \033[1m é uma sequência de escape ANSI que define o estilo do texto como negrito.
# \033[0m é uma sequência de escape ANSI que redefine o estilo do texto para o padrão (sem formatação).
# \033[3m é uma sequência de escape ANSI que define o estilo do texto como itálico.
# \n é um caractere de nova linha que move o cursor para a próxima linha.
# \t é um caractere de tabulação que move o cursor para a próxima posição de tabulação.
# Portanto, quando você executa print(mensagem), a mensagem é impressa com “Alvo Dumbledore:” em negrito e a citação em itálico.

