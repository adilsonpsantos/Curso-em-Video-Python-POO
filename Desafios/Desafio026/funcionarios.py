from abc import ABC, abstractmethod

from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    sal_minimo = 1612
    inss = 0.075

    def __init__(self, nome):
        self.nome = nome
        self.salario = 0
        self.sal_bruto = 0

    @abstractmethod
    def calcular_sal(self):
        pass

    def analisar_sal(self):
        razao =  self.salario/Funcionario.sal_minimo
        painel = Panel(f"O salário de [blue]{self.nome}[/] ([magenta]{self.__class__.__name__}[/]) é de [red]R${self.salario:.2f}[/]\n"
                         f"e corresponde a [yellow]{razao:.2f} salários mínimos[/].",
                         title= "Análise do Salário")
        print(painel)

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora = 12, qtd_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calcular_sal(self):
        self.salario = self.valor_hora * self.qtd_horas * (1 - Funcionario.inss)
        #return Funcionario.salario


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto = Funcionario.sal_minimo):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calcular_sal(self):
        self.salario = self.sal_bruto * (1 - Funcionario.inss)


