from rich import inspect
from funcionarios import *

def main():
    f1 = FuncionarioHorista('Fernando', 10, 200)
    f2 = FuncionarioMensalista("Ana", 10000)

    f1.calcular_sal()
    f1.analisar_sal()
    f2.calcular_sal()
    f2.analisar_sal()
    #inspect(f1)
    #inspect(f2)
if __name__ == '__main__':
    main()