from rich import print, inspect
from classes import Aluno, Professor, Funcionario

def main():
    a1 = Aluno("José", 17, "Informática", "T01")
    p1 = Professor("Gustavo", 43, "Biologia", "mestrado")
    f1 = Funcionario("Debora", 34, "secretária", "contabilidade")
    #print(a1.__dict__)
    #inspect(a1, methods=True)
    a1.fazer_aniversario()
    p1.fazer_aniversario()
    f1.fazer_aniversario()

    a1.fazer_matricula()
    p1.dar_aula()
    f1.bater_ponto()

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == '__main__':
    main()