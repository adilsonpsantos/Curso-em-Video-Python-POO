from personagem_rpg import *
from rich import inspect


def main():
    p1 = Guerreiro("Vader", 200)
    p2 = Mago("Yoda", 200)
    p1.atacar(p2, 150)
    p1.atacar(p2, 150)
    p1.atacar(p2, 150)
    p1.curar()
    p2.curar()
    #p1.receber_dano(100)
    #inspect(p1, methods=True)



if __name__ == '__main__':
    main()