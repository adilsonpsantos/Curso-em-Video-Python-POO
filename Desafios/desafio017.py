from rich import print
from rich.panel import Panel

class Produto():
    """
    gera etiquetas de produtos
    """
    def __init__(self,nome,valor,desconto = 0.00):
        self.nome = nome
        self.valor = "R$ " + str(f"{valor:,.2f}")
        self.desconto = desconto

    def __str__(self):
        # sobreescrita do método str da classe
        return f"{self.nome} custa {self.valor}"

    def etiqueta(self):
        etiqueta = Panel(f"{self.nome:^30}\n"
                      f"------------------------------\n"
                      f"{self.valor:.^30}",
                      title = "Produto",
                      #title_align="center",
                      expand = False
                      )
        print(etiqueta)

        # outra forma de fazer
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        conteudo += f"{self.valor.center(30, '.')}"
        etiqueta2 = Panel(conteudo, title="Produto *", width=34)

        print(etiqueta2)

p1 = Produto("Notebook Gamer", 5_499.90)
p1.etiqueta()
print(p1)