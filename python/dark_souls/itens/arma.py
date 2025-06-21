from .item import Item  

class Arma(Item):  
    def __init__(self, nome: str, dano: int):
        super().__init__(nome, "arma")
        self.dano = dano

    def usar(self):  
        print(f"{self.nome} foi empunhada e causa {self.dano} de dano!")
        return self.dano
