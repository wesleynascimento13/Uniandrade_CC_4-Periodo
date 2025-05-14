class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 10
        self.vivo = True

    def usar_pocao(self, pocao):
        self.saude += pocao.potencia
        print(f"Personagem {self.nome} usou poção {pocao.tipo}")
        print(f"Dano {pocao.potencia} saúde {self.saude}")

class PocaoVerde:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

# Crie uma nova PocaoRoxa

# Instanciar Jogador
p1 = Personagem("Chaves")
pocao1 = PocaoVerde("Cura", 15)
# p1.usar_pocao(pocao1)

del p1
print(pocao1)
