from rich import print
from rich.panel import Panel
import os


class ControleRemoto:
    """
    Simula o funcionamento de um controle remoto de televisão
    """
    # atributos de classe
    canal_min: int = 1
    canal_max: int = 6
    vol_min: int = 1
    vol_max: int = 5

    def __init__(self):
        # atributos de instância
        self.status = "desligada"
        self.ch = 1
        self.vol = 1
        self.ligado:bool = False

        self.painel_off()

    def mostrar_tv(self):
        if self.ligado:
            self.painel()

    def painel(self, status):
        os.system('cls' if os.name == 'nt' else 'clear')


    def painel_off(self):
        """
        exibe na tela o painel indicando que a TV está desligada
        :return:
        """
        # Detecta o sistema operacional e executa o comando apropriado
        os.system('cls' if os.name == 'nt' else 'clear')
        tv = Panel(f":prohibited: [red]A TV está desligada[/]",
                   title=" [ TV ] ",
                   title_align="center",
                   width=40
                   )
        print(tv)
        self.comandos("off")

    def painel_on(self):
        """
        exibe na tela o painel indicando que a TV está ligada
        :return:
        """
        # Detecta o sistema operacional e executa o comando apropriado
        os.system('cls' if os.name == 'nt' else 'clear')
        tv = Panel(f"CANAL  = {self.display_canal()}\n" +
                   f"VOLUME = {self.display_volume()}",
                   title=" [ TV ] ",
                   title_align="center",
                   width=40
                   )
        print(tv)
        self.comandos("on")

    def comandos(self, painel):
        comando = input(f" < CH{self.ch} >    - VOL{self.vol} +  ")
        if painel == "on":
            if comando == "<" or comando == ">":
                self.canal(comando)
                self.painel_on()
            elif comando == "+" or comando == "-":
                self.volume(comando)
                self.painel_on()

        if comando == "@":
            self.ligar_desligar()
        elif comando.upper() == "0":
            exit()
        else:
            if painel == "on":
                self.painel_on()
            else:
                self.painel_off()

    def ligar_desligar(self):
        if self.status == "desligada":
            # liga a TV
            self.status = "ligada"
            self.painel_on()

        else:
            # desliga a TV
            self.status = "desligada"
            self.painel_off()

    def canal(self, botao):
        if botao == ">":
            if self.ch < ControleRemoto.canal_max:
                self.ch += 1
            else:
                self.ch = ControleRemoto.canal_min
        elif botao == "<":
            if self.ch > ControleRemoto.canal_min:
                self.ch -= 1
            else:
                self.ch = ControleRemoto.canal_max

        self.display_canal()

    def display_canal(self):
        self.ind_canal = ""
        for i in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
            if i == self.ch:
                self.ind_canal += "[bold white on blue] " + str(self.ch) + " [/] "
            else:
                self.ind_canal += " " + str(i) + " "
        return self.ind_canal

    def volume(self, botao):
        if botao == "+" and self.vol < 5:
            self.vol += 1
        elif botao == "-" and self.vol > 1:
            self.vol -= 1

    def display_volume(self):
        # atualiza o indicador de volume
        self.ind_volume = f"[white on green][white on red]{'  ' * self.vol}[/]{'  ' * (5 - self.vol)}[/]"
        return self.ind_volume

tv = ControleRemoto()
