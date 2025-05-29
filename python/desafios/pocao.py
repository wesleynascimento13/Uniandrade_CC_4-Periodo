import os
import time

class Item:
    def __init__(self, tipo: str, efeito: int):
        self.tipo = tipo
        self.efeito = efeito

class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: Item):
        if item:
            self.itens.append(item)

    def listar_itens(self):
        print("\nInventário:")
        if not self.itens:
            print("Vazio.")
        for item in self.itens:
            print(f"- {item.tipo} (Efeito: {item.efeito})")

class Armadura:
    def __init__(self, nome: str, protecao: int):
        self.nome = nome
        self.protecao = protecao

class Pocao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class Personagem:
    def __init__(self, nome, nome_armadura: str = "Armadura Comum", protecao: int = 10):
        self.nome = nome
        self.saude = 100
        self.vivo = True
        self.armadura = Armadura(nome_armadura, protecao)
        self.inventario = Inventario()

    def mostrar_vida(self):
        barra = int(self.saude / 5)
        print(f"\n{self.nome} | Saúde: {self.saude}/100")
        print("[" + "█" * barra + " " * (20 - barra) + "]")

    def mostrar_status(self):
        estado = "VIVO" if self.vivo else "MORTO"
        print(f"\nStatus de {self.nome}")
        print(f"- Estado: {estado}")
        print(f"- Armadura: {self.armadura.nome} (+{self.armadura.protecao})")
        self.mostrar_vida()
        self.inventario.listar_itens()

    def usar_pocao(self, pocao):
        if not self.vivo:
            print(f"{self.nome} está morto e não pode usar poções.")
            return

        print(f"\n{self.nome} usou Poção {pocao.tipo}")

        if pocao.tipo == "Cura":
            cura = min(pocao.valor, 100 - self.saude)
            self.saude += cura
            print(f"Curou {cura} pontos de vida.")
        elif pocao.tipo == "Dano":
            self.saude -= pocao.valor
            print(f"Sofreu {pocao.valor} de dano mágico.")
            if self.saude <= 0:
                self.saude = 0
                self.vivo = False
                print(f"{self.nome} morreu!")
        else:
            print(f"Tipo de poção '{pocao.tipo}' desconhecido.")

        self.mostrar_vida()

# ========== INÍCIO ==========

p1 = Personagem("Persel", "Armadura do Rei", 15)
p1.inventario.adicionar_item(Item("Faca Tramontina", 120))
p1.inventario.adicionar_item(Item("Escudo do Rei", 90))

pocao_verde = Pocao("Cura", 20)   # Cura fixa de 20
pocao_roxa = Pocao("Dano", 30)   # Dano mágico fixo de 30

while p1.vivo:
    os.system("cls" if os.name == "nt" else "clear")
    p1.mostrar_status()

    print("\nEscolha uma poção:")
    print("1 - Poção Verde (+20)")
    print("2 - Poção Roxa (-30)")
    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        p1.usar_pocao(pocao_verde)
    elif escolha == "2":
        p1.usar_pocao(pocao_roxa)
    else:
        print("Opção inválida!")

    time.sleep(1)

print("\nFim do jogo.")
