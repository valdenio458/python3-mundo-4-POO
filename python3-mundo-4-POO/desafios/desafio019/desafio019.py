from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [red]'{self.titulo}'[/red] que tem "
              f"[green]{self.total_paginas} paginas[/] no total. Você agora está na [yellow]pagina {self.pagina_atual}[/][/blue]")

    def avancar_paginas(self, qtd = 1 ):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
              self.pagina_atual += 1
              print(f"Pág{self.pagina_atual} :arrow_forward: ", end='')
              time.sleep(0.3)
              cont += 1
        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]pagina {self.pagina_atual}[/]")
        if self.fim_do_livro():
            print(f":closed_book: [red] Você chegou ao final do livro '{self.titulo}'![/]")
    def fim_do_livro(self) -> bool:
        #  if self.pagina_atual == self.total_paginas:
        #    return True
        # else:
        #    return False
       return True if self.pagina_atual == self.total_paginas else False


l1 = Livro("10 coisas que aprendi", 20)
print(l1)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)

