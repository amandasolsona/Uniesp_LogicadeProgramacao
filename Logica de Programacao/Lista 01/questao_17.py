#Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão,
# chame este dicionário de glossário.
#Pense em cinco palavras relacionadas à programação que você conhece. Use estas palavras como chaves em seu glossário e
# armazene seus significados como valores.
#Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante. Por exemplo: você pode
# exibir a palavra seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma linha e então
# exibir seu significado identado em uma segunda linha. Utilize o caractere de quebra de linha (\n) para inserir uma
# linha em branco entre cada palavra-significado em sua saída.
#Sugestões de termos: Algoritmos, Python, Web Scraping, Lógica de Programação, Google Colab, Visual Studio Code.

glossario = {'Algoritmos': 'É uma sequência de instruções bem definidas,'
                           ' normalmente usadas para resolver problemas de matemática específicos,'
                           ' executar tarefas, ou para realizar cálculos e equações.',
             'Python': 'É uma linguagem de programação de alto nível, interpretada de script,'
                       ' imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.',
             'Lógica de Programação': ' É onde aplicamos todos os conceitos de algoritmos, a definição'
                                      ' do passo a passo e transferimos toda a lógica do algoritmo desenvolvido'
                                      ' para uma linguagem de programação.',
             'Java': 'É uma linguagem multiplataforma, orientada a objetos e centrada em rede'
                     ' que pode ser usada como uma plataforma em si. É uma linguagem de programação rápida,'
                     ' segura e confiável para codificar tudo, desde aplicações móveis e'
                     ' software empresarial até aplicações de big data e tecnologias do servidor.',
             'Web Scraping': 'É uma ferramenta muito utilizada em estratégias de transformação digital'
                             ' e também para automatizar processos de coleta e consulta de dados e'
                             ' informações públicas, para diversos fins.'
             }

for chave in glossario.keys():
    print(f'{chave} :\n {glossario[chave]}')