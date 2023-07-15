class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")


#Função em Python = Método em Java;
#Ex: def
#__init__ é um construtor que é executado quando um objeto da classe é criado;
#Metodo não é obrigatório retornar algo;

