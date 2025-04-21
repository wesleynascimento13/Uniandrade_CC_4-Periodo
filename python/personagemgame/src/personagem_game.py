import sys
import os

LIB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib'))
sys.path.insert(0, LIB_PATH)


class PersonagemMarvel:
    def __init__(self, nome, afiliacao, poder_principal, vida):
        self.nome = nome
        self.afiliacao = afiliacao
        self.poder_principal = poder_principal
        self.vida = vida
        self.habilidades = []
        self.inventario = []

    def usar_habilidade(self, habilidade, alvo):
        print(f"{self.nome} utilizou '{habilidade}' contra {alvo}!")

    def adicionar_item_inventario(self, nome, tipo, efeito):
        item = {"nome": nome, "tipo": tipo, "efeito": efeito}
        self.inventario.append(item)

    def listar_inventario(self):
        if not self.inventario:
            return "Inventário vazio"
        item = self.inventario[0]
        return f"- {item['nome']} ({item['tipo']}): {item['efeito']}"

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Afiliação: {self.afiliacao}")
        print(f"Poder Principal: {self.poder_principal}")
        print(f"Vida: {self.vida}")
        print("Habilidades:", ", ".join(self.habilidades))
        print("Inventário:\n")
        print(self.listar_inventario())
        print("-" * 40)


groot = PersonagemMarvel("Groot", "Guardiões da Galáxia", "Resistência e controle de grupo", 700)
rocket = PersonagemMarvel("Rocket Raccoon", "Guardiões da Galáxia", "Alto dano por segundo", 250)

groot.habilidades.extend(["Crescimento de Raízes", "Escudo de Galhos"])
rocket.habilidades.extend(["Canhão de Plasma", "Granada de Gravidade"])

groot.adicionar_item_inventario("Galho Protetor", "Defensivo", "Reduz dano em 60% por 7 segundos")
rocket.adicionar_item_inventario("Granada de Fragmentação", "Explosivo", "Causa 150 de dano em área")

groot.status()
rocket.status()

groot.usar_habilidade("Crescimento de Raízes", "Rocket Raccoon")
rocket.usar_habilidade("Granada de Gravidade", "Groot")
