from .item import Item

class Pocao(Item):
    def __init__(self, nome: str, cura: int):
        super().__init__(nome, "pocao")
        self.cura = cura

    def usar(self, jogador):
        jogador.saude = self.cura
        print(f"{jogador.nome} usou {self.nome} e recuperou {self.cura} de vida!")
