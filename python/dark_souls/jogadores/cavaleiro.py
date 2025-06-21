from .jogador import Jogador  

class Cavaleiro(Jogador):  
    def __init__(self, nome: str, dano: int):
        super().__init__(nome, dano)
        self.saude = 100  # A saúde inicial do cavaleiro
        self.gold = 0  # O gold do cavaleiro
        self.especial = 0  # A barra de especial (deve começar em 0)

    def atacar(self):  
        print(f"{self.nome} atacou com sua espada!")
        dano = self.dano
        self.especial = min(100, self.especial + 20)  # Aumenta a barra especial a cada ataque
        return dano  # Retorna o dano corretamente

    def defender(self):  
        print(f"{self.nome} defendeu com seu escudo!")
        # Implemente a lógica para reduzir a saúde do cavaleiro com base no dano do inimigo
        # Por exemplo, se um inimigo ataca com 20 de dano:
        # self.saude -= 20
        pass

    def usar_poção(self, pocao):
        """Método para usar poções, que recuperam saúde"""
        self.saude = min(100, self.saude + pocao.cura)
        pocao.quantidade -= 1  # Reduz a quantidade da poção após o uso
        print(f"{self.nome} usou {pocao.nome} e recuperou {pocao.cura} de saúde!")

if __name__ == "__main__":
    cavaleiro = Cavaleiro("Rei Artur", 80)
    cavaleiro.atacar()
    print(f"Especial: {cavaleiro.especial}")  # Mostra o valor do especial
