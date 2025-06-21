class NPC:
    def __init__(self, dialogo: str, amizade: int):
        self.dialogo = dialogo
        self.amizade = amizade

    def falar(self):
        print(f"NPC diz: {self.dialogo}")
