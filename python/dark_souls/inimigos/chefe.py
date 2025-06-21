import random
from .inimigo import Inimigo

class Chefe(Inimigo):
    def __init__(self, nome: str, dano: int):
        super().__init__(nome, dano, saude=200)

    def atacar(self):
        tipo = random.choice(["básico", "forte", "especial"])
        if tipo == "básico":
            dano = max(0, self.dano - 10)
        elif tipo == "forte":
            dano = max(0, self.dano + 10 - 10)
        else:
            dano = max(0, self.dano * 2 - 10)
        print(f"{self.nome} usou ataque {tipo} causando {dano} de dano!")
        return dano

    def prever_ataque(self):
        tipo = random.choice(["básico", "forte", "especial"])
        if tipo == "básico":
            dano = max(0, self.dano - 10)
        elif tipo == "forte":
            dano = max(0, self.dano + 10 - 10)
        else:
            dano = max(0, self.dano * 2 - 10)
        print(f"{self.nome} preparou ataque {tipo} que causaria {dano} de dano!")
