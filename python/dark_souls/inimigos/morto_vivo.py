import random
from .inimigo import Inimigo

class MortoVivo(Inimigo):
    def __init__(self, nome: str, dano: int, saude: int, ataques: list):
        super().__init__(nome, dano, saude)
        self.ataques = ataques

    def atacar(self):
        ataque = random.choice(self.ataques)
        dano_total = self.dano + ataque['bonus']
        print(f"{self.nome} usou {ataque['nome']} causando {dano_total} de dano!")
        return dano_total
