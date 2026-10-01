from rich import print
from rich import inspect

class Funcionario:
    """
    Cria e gerencia funcionários
    """
    # Atributos de class
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá, sou [bold blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa} :laptop_computer:"
        #return f":handshake: Olá, sou [bold blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa} :laptop_computer:"


c1 = Funcionario("Maria", "Administração", "Diretora")
#c1.empresa = "Boing"
#inspect(c1, methods=True)
#print(c1.__dict__)
c1.apresentacao()
print(c1.apresentacao())

c2 = Funcionario("Adilson", "TI", "Programador")
print(c2.apresentacao())
