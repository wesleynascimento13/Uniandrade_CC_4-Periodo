from .inimigo import Inimigo

class MortoVivo(Inimigo):
    def __init__(self, nome: str, dano: int, podridao: int):
        super().__init__(nome, dano)
        self.podridao = podridao

    def morder(self):
        dano_total = self.dano + self.podridao
        print(f"{self.nome} mordeu causando {dano_total} de dano!")
        return dano_total
