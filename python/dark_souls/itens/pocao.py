from .item import Item

class Pocao(Item):
    def __init__(self, nome: str, cura: int, quantidade: int):
        super().__init__(nome, "pocao")
        self.cura = cura
        self.quantidade = quantidade

    def usar(self, jogador):
        if self.quantidade > 0:
            jogador.saude = self.cura
            self.quantidade -= 1
            print(f"{jogador.nome} usou {self.nome} e recuperou {self.cura} de vida!")
        else:
            print(f"{self.nome} acabou!")
