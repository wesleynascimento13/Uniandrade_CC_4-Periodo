import random
from .inimigo import Inimigo

class MortoVivo(Inimigo):
    def __init__(self, nome: str, dano: int, saude: int, ataques: list):
        super().__init__(nome, dano, saude)
        self.ataques = ataques

    def _validar_ataques(self):
        """Método privado para validar a estrutura dos ataques."""
        for ataque in self.ataques:
            if 'nome' not in ataque or 'bonus' not in ataque:
                raise ValueError("Cada ataque deve ter 'nome' e 'bonus'.")

    def atacar(self):
        self._validar_ataques()  # Valida os ataques antes de usar
        ataque = random.choice(self.ataques)
        dano_total = self.dano + ataque['bonus']
        print(f"{self.nome} usou {ataque['nome']} causando {dano_total} de dano!")
        return dano_total

    def prever_ataque(self):
        """Previsão de ataque do MortoVivo baseado nos ataques disponíveis"""
        ataque = random.choice(self.ataques)
        dano_previsto = self.dano + ataque['bonus']
        print(f"{self.nome} preparou ataque {ataque['nome']} que causaria {dano_previsto} de dano!")
