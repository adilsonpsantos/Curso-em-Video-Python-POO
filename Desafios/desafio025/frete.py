from transportes import *
from rich import print, inspect
from rich.table import Table

def main():
    dist = 50
    frete = 12
    """
    entrega = Moto(dist, frete)
    print(f"Frete de {dist}km com {type(entrega).__name__} = {entrega.calcular_frete()}")

    entrega = Caminhao(dist, frete)
    print(f"Frete de {dist}km com {type(entrega).__name__} = {entrega.calcular_frete()}")

    entrega = Drone(dist, frete)
    print(f"Frete de {dist}km com {type(entrega).__name__} = {entrega.calcular_frete()}")

    entrega = [Moto(dist, frete), Caminhao(dist, frete), Drone(dist, frete)]
    """
    #   uma forma mais bonita

    entrega = [Moto(dist, frete), Caminhao(dist, frete), Drone(dist, frete)]

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distancia (km)", justify="center")
    tabela.add_column("Tipo", justify="center")
    tabela.add_column("Frete (R$)", justify="center")

    for item in entrega:
        tabela.add_row(f"{dist}", f"{type(item).__name__}", f"{item.calcular_frete()}")

    print(tabela)

if __name__ == "__main__":
    main()