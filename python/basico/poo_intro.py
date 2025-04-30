class Player:
    host = "localhost:8080"  # Global

    # inicializador do objeto
    # passando valores posicionais
    def __init__(self, nome, arma):
        self.nome = nome  # autoriza modificação/objeto
        self.arma = arma

kratos: Player = Player("kratos", "Lâminas do caos")
Hades: Player = Player("Hades", "Styguis")

print(kratos.nome, kratos.arma)
print(Hades.nome, Hades.host)
