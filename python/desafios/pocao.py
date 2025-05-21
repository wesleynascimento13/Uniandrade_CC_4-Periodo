import os
import time

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 100
        self.vivo = True

    def mostrar_vida(self):
        barra = int(self.saude / 5)  
        print(f"\n{self.nome} | Saúde: {self.saude}/100")
        print("[" + "█" * barra + " " * (20 - barra) + "]")

    def usar_pocao(self, pocao):
        if not self.vivo:
            print(f"{self.nome} está morto e não pode usar poções.")
            return

        if pocao.tipo == "cura":
            if self.saude >= 100:
                print(f"{self.nome} já está com a saúde cheia. Poção de cura não teve efeito.")
            else:
                cura_real = min(pocao.potencia, 100 - self.saude)
                self.saude += cura_real
                print(f"{self.nome} usou Poção Verde (+{cura_real})")
        elif pocao.tipo == "veneno":
            self.saude -= pocao.potencia
            print(f"{self.nome} tomou Poção Roxa (-{pocao.potencia})")
            if self.saude <= 0:
                self.saude = 0
                self.vivo = False
                print(f"{self.nome} morreu!")
        else:
            print(f"Tipo de poção '{pocao.tipo}' desconhecido.")

        self.mostrar_vida()

class Pocao:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
        
# ========== INÍCIO ==========
p1 = Personagem("Chaves")
pocao_verde = Pocao("cura", 20)
pocao_roxa = Pocao("veneno", 30)

while p1.vivo:
    print("\nEscolha uma poção:")
    print("1 - Poção Verde (+20)")
    print("2 - Poção Roxa (-30)")
    escolha = input("Digite sua escolha: ")

    os.system("cls" if os.name == "nt" else "clear")

    if escolha == "1":
        p1.usar_pocao(pocao_verde)
    elif escolha == "2":
        p1.usar_pocao(pocao_roxa)
    else:
        print("Opção inválida!")

    time.sleep(0.5)

print("\nFim do jogo.")
