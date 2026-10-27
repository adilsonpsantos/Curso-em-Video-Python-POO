from cafeteria import *
#from rich import print, inspect
#from rich.panel import Panel

def main():
    b1 = Leite()
    b2 = Cafe()
    b3 = Cha()
    b1.preparar()
    b2.preparar()
    b3.preparar()
"""
import cafeteria

def main():
    b1 = cafeteria.Leite()
    b2 = cafeteria.Cafe()
    b3 = cafeteria.Cha()
    b1.preparar()
    b2.preparar()
    b3.preparar()
"""
if __name__ == '__main__':
    main()