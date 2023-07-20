import json
import re


class Aluno:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


def verificar_cpf(cpf):
    if len(cpf) != 11:
        raise ValueError('O CPF deve ter 11 dígitos')


def verificar_email(email):
    padrao_email = re.compile(r'[^@]+@[^@]+\.[^@]+')
    if not padrao_email.match(email):
        raise ValueError('Endereço de e-mail inválido')


class Cadastro:
    def __init__(self):
        self.alunos = []

    def cadastrar_aluno(self):
        nome = input('Digite o nome do aluno: ')
        cpf = input('Digite o cpf do aluno: ')
        self.verificar_cpf(cpf)
        email = input('Digite o email do aluno: ')
        self.verificar_email(email)
        aluno = Aluno(nome, cpf, email)
        self.alunos.append(aluno)
        return self

    def salvar_alunos(self):
        with open('alunos.json', 'w') as file_object:
            json.dump([aluno.__dict__ for aluno in self.alunos], file_object)

    def remover_aluno(self):
        nome = input('Digite o nome do aluno que deseja remover: ')
        for aluno in self.alunos:
            if aluno.nome == nome:
                self.alunos.remove(aluno)
                break

    def editar_aluno(self):
        nome = input('Digite o nome do aluno que deseja editar: ')
        for aluno in self.alunos:
            if aluno.nome == nome:
                novo_nome = input('Digite o novo nome do aluno: ')
                aluno.nome = novo_nome
                break

    def listar_alunos(self):
        for aluno in self.alunos:
            print(aluno.nome)


cadastro = Cadastro()

while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar Aluno")
    print("2 - Remover Aluno")
    print("3 - Editar Aluno")
    print("4 - Listar Aluno")
    print("5 - Salvar Alunos")
    print("6 - Sair")

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        try:
            cadastro.cadastrar_aluno()
        except ValueError as exception:
            print(f"Ocorreu um erro: {exception.args[0]}")
    elif opcao == 2:
        cadastro.remover_aluno()
    elif opcao == 3:
        cadastro.editar_aluno()
    elif opcao == 4:
        cadastro.listar_alunos()
    elif opcao == 5:
        cadastro.salvar_alunos()
    elif opcao == 6:
        break
