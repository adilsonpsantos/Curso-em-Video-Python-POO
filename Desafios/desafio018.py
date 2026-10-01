from rich import print
from rich.panel import Panel

class Churrasco():

    # Atributos de classe
    consumo:float = 0.4
    preco:float = 82.40
    
    def __init__(self, titulo = "", quantidade = 2):
        # Atributos de instância
        self.titulo = titulo
        self.quantidade = quantidade

    def __str__(self) -> str:
        return f"este é o {self.titulo} com {self.quantidade} pessoas participando"
    
    def analisar(self):
        self.total_carne = self.quantidade * Churrasco.consumo # ou self.__class__.consumo
        self.custo_total = self.total_carne * Churrasco.preco
        self.custo_pessoa = Churrasco.consumo * Churrasco.preco
        mensagem = Panel(f"Analisando [green]Churras com Amigos[/] com [blue]{self.quantidade}[/] convidados\n"
                         f"Cada participante comerá {Churrasco.consumo}kg e cada kg custa R${Churrasco.preco:.2f}\n"
                         f"Recomendo [blue]comprar {self.total_carne:.1f}kg[/] de carne\n"
                         f"O custo total será de [green]R${self.custo_total:.2f}[/]\n"
                         f"Cada pessoa pagará [red]R${self.custo_pessoa:.2f}[/] para participar",
                         title = self.titulo,
                         title_align= "center",
                         expand=False)
        print(mensagem)

churras = Churrasco("Churras dos Amigos", 15)
churras.analisar()