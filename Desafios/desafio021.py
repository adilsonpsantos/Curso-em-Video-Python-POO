from rich import print

class Caneta:

    def __init__(self, cor = 'branca'):
        self.cor = cor
        self.tampa = True
        self.colors = {
            'vermelha': 'red',
            'vermelho': 'red',
            'verde': 'green',
            'azul': 'blue',
            'amarelo': 'yellow',
            'amarela': 'yellow',
            'branco': 'white',
            'branca': 'white'
        }

        try:
            self.color = self.colors[cor]
        except KeyError:
            self.color = 'white'
        # outra opção para fazer a codificação das cores usando 'match'. Esta opção dispensa o uso do 'try - except'
        """
        match cor.lower().strip():
            case "azul":
                self.color = '[blue]'
            case "vermelho":
                self.color = '[red]'
            case _:
                self.color = '[white]'
        """

    def destampar(self):
        self.tampa = False

    def tampar(self):
        self.tampa = True

    def escrever(self, texto):
        if not self.tampa:
            print(f"[{self.color}]{texto}[/]", end='')
        else:
            print(f":prohibited: A [{self.color}]caneta[/] está tampada!", end='')

    def quebrar_linha(self, qtd = 1):
        print("\n" * qtd)

c1 = Caneta('vermelho')
c2 = Caneta('amarelo')
c3 = Caneta('azul')
#c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha()
c2.escrever("Vamos escrever?")
c2.quebrar_linha()
c3.escrever("Está pronto?")

c1.tampar()
c2.tampar()
c3.tampar()

