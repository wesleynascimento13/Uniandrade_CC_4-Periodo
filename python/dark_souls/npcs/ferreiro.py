from .npc import NPC

class Ferreiro(NPC):
    def __init__(self, dialogo: str, amizade: int, inventario: list):
        super().__init__(dialogo, amizade)
        self.inventario = inventario

    def vender_item(self):
        print("Ferreiro vendeu um item!")
