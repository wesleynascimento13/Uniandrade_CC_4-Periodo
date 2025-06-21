from abc import ABC, abstractmethod

class Jogador(ABC):
    def __init__(self, nome: str, dano: int):
        self.nome = nome
        self.dano = dano
        self.__saude = 100

    @property
    def saude(self):
        return self.__saude

    @saude.setter
    def saude(self, valor):
        self.__saude = max(0, min(100, self.__saude + valor))

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self):
        pass
