from .jogador import Jogador  

class Cavaleiro(Jogador):  
    def __init__(self, nome: str, dano: int):
        super().__init__(nome, dano)

    def atacar(self):  
        print("Atacar Polimórfico")
        print(f"{self.nome} atacou com sua espada!")

    def defender(self):  
        print("Defender Polimórfico")
        print(f"{self.nome} defendeu com seu escudo!")

if __name__ == "__main__":
    cavaleiro = Cavaleiro("Rei Artur", 80)
    cavaleiro.atacar()
