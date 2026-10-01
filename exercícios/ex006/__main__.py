from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno("José", 17, "Informática", "T01")
    #print(a1.__dict__)
    #inspect(a1, methods=True)
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor("Gustavo", 43, "Biologia", "mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario("Debora", 34, "Supervisora", "Secretaria")
    f1.fazer_aniversario()
    f1.bater_ponto()

if __name__ == '__main__':
    main()