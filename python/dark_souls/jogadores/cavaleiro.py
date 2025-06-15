from jogador import Jogador

class Cavaleiro(Jogador):  # Herança
    def __init__(self, nome: str, dano: int):
        super().__init__(nome, dano)
        self.__saude = 100  # encapsulamento

    @property  # Decorador retorna apenas como propriedade
    def saude(self):
        return self.__saude

    @saude.setter  # Decorador retorna apenas como propriedade
    def saude(self, valor):
        self.__saude += max(0, valor)

    def atacar(self):
        print("Atacar Polimórfico")
        print(f"{self.nome} atacou")

    def defender(self):
        print("Defender Polimórfico")
        print(f"{self.nome} defendeu")

if __name__ == "__main__":
    cavaleiro = Cavaleiro("Rei Artur", 80)
    cavaleiro.atacar()
