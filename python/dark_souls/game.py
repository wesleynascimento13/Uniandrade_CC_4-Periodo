import random
from random import sample
from jogadores.cavaleiro import Cavaleiro
from itens.pocao import Pocao
from inimigos.chefe import Chefe
from inimigos.morto_vivo import MortoVivo

# ── util ──────────────────────────────────────────────────────────────────
def barra_de_vida(valor_atual, valor_maximo, largura: int = 20, *, cor: str = ''):
    proporcao  = max(0, valor_atual) / valor_maximo
    preenchido = int(proporcao * largura)
    vazio      = largura - preenchido
    barra      = '█' * preenchido + '░' * vazio
    return f"{cor}[{barra}] {valor_atual}/{valor_maximo}\033[0m"

# ── inimigos ──────────────────────────────────────────────────────────────
def escolher_inimigo():
    print("\n--- ESCOLHA SEU DESAFIO ---")
    print("1. Chefe: Senhor das Cinzas")
    print("2. Morto-Vivo (aleatório)")
    op = input("Número do inimigo: ")

    if op == "1":
        return Chefe("Senhor das Cinzas", 30), 200

    vivos = [
        ("Esqueleto Sombrio", 25, 120,
         [{"nome":"Mordida Enferrujada","bonus":5},
          {"nome":"Arranhão Maldito",  "bonus":10},
          {"nome":"Grito Espectral",   "bonus":0}]),
        ("Carniçal Rastejante", 20, 110,
         [{"nome":"Investida Podre","bonus":15},
          {"nome":"Lambida Tóxica","bonus":5},
          {"nome":"Esfarrapar",    "bonus":10}]),
        ("Zumbi Selvagem", 30, 100,
         [{"nome":"Cabeçada Podre","bonus":0},
          {"nome":"Mordida Fúria","bonus":10},
          {"nome":"Empurrão",     "bonus":5}]),
        ("Sombra Cadavérica", 22, 130,
         [{"nome":"Garras Etéreas","bonus":8},
          {"nome":"Sopro do Túmulo","bonus":4},
          {"nome":"Toque Gélido",  "bonus":6}]),
    ]
    nome, dano, vida, ataques = random.choice(vivos)
    return MortoVivo(nome, dano, vida, ataques), vida

# ── inventário e serviços ────────────────────────────────────────────────
def consultar_inv(inv, cav=None):
    print("\n--- INVENTÁRIO ---")
    if not inv:
        print("Vazio.")
    else:
        for i, p in enumerate(inv, 1):
            print(f"{i}. {p.nome} (+{p.cura}) – qtd {p.quantidade}")
    if cav is None:
        input("Enter para voltar…")
        return

    esc = input("Número da poção para usar ou Enter p/ voltar: ")
    if not esc.isdigit():
        return
    idx = int(esc) - 1
    if 0 <= idx < len(inv):
        inv[idx].usar(cav)
        if inv[idx].quantidade == 0:
            inv.pop(idx)
    else:
        print("Opção inválida.")

def comprar_pocoes(cav, inv):
    print("\n--- LOJA DE POÇÕES ---")
    opcoes = [("Poção Fraca", 20, 10),
              ("Poção Média", 40, 20),
              ("Poção Forte", 60, 30)]
    for i,(n,cura,preco) in enumerate(opcoes,1):
        print(f"{i}. {n} (+{cura}) – {preco} G")
    esc = input("Número ou Enter p/ voltar: ")
    if not esc.isdigit(): return
    idx = int(esc)-1
    if 0<=idx<len(opcoes):
        nome,cura,preco = opcoes[idx]
        if cav.gold < preco:
            print("Gold insuficiente.")
            return
        cav.gold -= preco
        inv.append(Pocao(nome,cura,1))
        print(f"Comprada {nome}.")
    else:
        print("Opção inválida.")

def ferreiro(cav):
    preco=50
    if cav.gold < preco:
        print("Gold insuficiente.")
        return
    cav.gold -= preco
    cav.dano += 10
    print("Arma aprimorada! +10 dano.")

def estalagem(cav):
    preco=30
    if cav.gold < preco:
        print("Gold insuficiente para dormir.")
        return
    cav.gold -= preco
    cav.saude = 100
    cav.especial = 0
    print("Você dormiu e se recuperou totalmente!")

# ── menus ────────────────────────────────────────────────────────────────
def menu_inicial(cav, inv):
    while True:
        print("\n"+"-"*42)
        print("Vida :", barra_de_vida(cav.saude,100,cor='\033[92m'))
        print("Esp  :", barra_de_vida(cav.especial,100,cor='\033[96m'))
        print(f"Gold : {cav.gold} G")
        print("-"*42)
        print("1. Iniciar batalha")
        print("2. Loja de poções")
        print("3. Ferreiro (+10 dano - 50G)")
        print("4. Estalagem (curar 30G)")
        print("5. Inventário")
        print("6. Sair")
        op = input("Escolha: ")

        if op=="1": return True
        if op=="2": comprar_pocoes(cav,inv)
        elif op=="3": ferreiro(cav)
        elif op=="4": estalagem(cav)
        elif op=="5": consultar_inv(inv)
        elif op=="6": return False
        else: print("Inválido.")

def batalha(cav, inv):
    inimigo, vida_max = escolher_inimigo()
    cav.especial = 0
    while True:
        print("\n"+"-"*42)
        print(f"{inimigo.nome:18}:",
              barra_de_vida(inimigo.saude,vida_max,cor='\033[91m'))
        print("Cavaleiro :", barra_de_vida(cav.saude,100,cor='\033[92m'))
        print("Especial  :", barra_de_vida(cav.especial,100,cor='\033[96m'))
        print("-"*42)
        print("1. Atacar  2. Defender  3. Inventário  4. Sair")
        if cav.especial>=100:
            print("5. ATAQUE ESPECIAL")
        op=input("Ação: ")

        if op=="1":
            cav.atacar()
            inimigo.saude = -cav.dano            # lógica solicitada
            cav.especial = min(100,cav.especial+20)
            if inimigo.saude>0:
                cav.saude = -inimigo.atacar()
        elif op=="2":
            cav.defender()
            if hasattr(inimigo,"prever_ataque"):
                inimigo.prever_ataque()
        elif op=="3":
            consultar_inv(inv,cav)
            continue
        elif op=="4":
            print("Você fugiu!")
            return
        elif op=="5" and cav.especial>=100:
            print("ATAQUE ESPECIAL!")
            inimigo.saude = -cav.dano*2          # mesma lógica
            cav.especial = 0
            if inimigo.saude>0:
                cav.saude = -inimigo.atacar()
        else:
            print("Inválido."); continue

        if cav.saude<=0:
            print("Derrota…"); return
        if inimigo.saude<=0:
            print(f"Vitória sobre {inimigo.nome}! +50G")
            cav.gold += 50
            return

# ── principal ────────────────────────────────────────────────────────────
def main():
    player = Cavaleiro("Rei Artur",20)
    global inventario
    inventario = sample([
        Pocao("Poção Fraca",20,1),
        Pocao("Poção Média",40,1),
        Pocao("Poção Forte",60,1)
    ],k=3)

    while menu_inicial(player,inventario):
        batalha(player,inventario)
        if player.saude<=0:
            break

if __name__=="__main__":
    main()
