from poligono import *
from rich import print, inspect

from rich.panel import Panel

def poligono(objeto):
    nome_poligono = objeto.__class__.__name__
    painel = Panel(f"Perímetro do {nome_poligono} = [blue]{objeto.perimetro():.2f}[/]\n"
                   f"Área do {nome_poligono} "
                   f"= {objeto.area():.2f}",
                   title = nome_poligono)
    print(painel)

def main():
    p1 = Quadrado(6)
    p2 = Circulo(3)
    print(p1.lado)
    #inspect(p1, methods=True)
    #inspect(p2, methods=True)

    poligono(p1)
    poligono(p2)

if __name__ == "__main__":
    main()