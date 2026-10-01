from rich import print
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem {self.paginas} páginas no total. "
              f"Você agora está na [/][yellow]página {self.pagina_atual}[/]")


    def avancar_paginas(self, num_paginas):
        pagina_inicial = self.pagina_atual
        mensagem = ""
        p = 0
        while (self.pagina_atual < self.paginas) and (self.pagina_atual < pagina_inicial + num_paginas):
            self.pagina_atual += 1
            p += 1
            mensagem += f"Pag {self.pagina_atual} :arrow_forward: "
        print(mensagem + f"\n[blue]Você avançou {p} páginas e agora está na [/][yellow]página {self.pagina_atual}[/]")
        if self.pagina_atual == self.paginas:
            print(f":arrow_forward: [red]Você chegou ao final do livro '{self.titulo}'[/]")


livro = Livro("10 coisas que aprendi", 20)
livro.avancar_paginas(8)
livro.avancar_paginas(5)
livro.avancar_paginas(20)
