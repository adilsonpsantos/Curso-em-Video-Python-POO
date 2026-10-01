from rich import print
from rich.panel import Panel

class Gamer():

    def __init__(self, nome, nick):
        self.name = nome
        self.nick = nick
        self.favoritos = list()

    def add_favorito(self, favorito):
        self.favoritos.append(favorito)

    def ficha(self):
        self.favoritos.sort()
        fav = ""
        for f in self.favoritos:
            fav += f"\n:video_game: [blue]{f}[/]"
        #print(fav)
        jogador = Panel(f"Nome real: [black on blue]{self.name}[/]\n"
                        f"Jogos favoritos:"
                        f"{fav}",
                        title = f"Jogador <{self.nick}>",
                        title_align="center",
                        width=40)
        print(jogador)


j1 = Gamer("Adilson", "Khan")
j1.add_favorito("Mario Bros")
j1.add_favorito("Sonic")
j1.add_favorito("God of War")
j1.add_favorito("Fortnite")
j1.ficha()

j2 = Gamer("Margareth", "Mag")
j2.add_favorito("Cats Run")
j2.add_favorito("Call o Duty")
j2.add_favorito("Alice in Chains")
j2.ficha()