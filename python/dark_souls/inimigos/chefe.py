from .inimigo import Inimigo

class Chefe(Inimigo):
    def ataque_especial(self):
        dano = self.dano * 2
        print(f"{self.nome} usou ataque especial causando {dano} de dano!")
        return dano
