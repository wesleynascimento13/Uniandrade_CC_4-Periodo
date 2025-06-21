class Inimigo:
    def __init__(self, nome: str, dano: int):
        self.nome = nome
        self.dano = dano
        self.__saude = 400

    @property
    def saude(self):
        return self.__saude

    @saude.setter
    def saude(self, valor):
        self.__saude = max(0, self.__saude + valor)

    def atacar(self):
        print(f"{self.nome} atacou com {self.dano} de dano!")
        return self.dano
