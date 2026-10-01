from abc import ABC, abstractmethod     # Abstract Base Classes

class Pessoa(ABC): # definição da classe Pessoa como abstrata
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez aniversário e agora está com {self.idade} anos de idade")

    @abstractmethod  # decorator necesessário para definir o método abstrado
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} acabou de fazer a matrícula")

    def estudar(self):
        print(f"{self.nome} está estudando {self.curso} na turma {self.turma}")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} começou a dar aula")

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade} no nível {self.nivel}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} registrou o ponto")

    def estudar(self):
        print(f"{self.nome} se especializa para a área de {self.setor}")
