class Item:
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo

    def usar(self):
        print(f"{self.nome} foi usado!")
