import sys
import os
import random

LIB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib'))
sys.path.insert(0, LIB_PATH)

from personagem import PersonagemMarvel

def escolher_personagem():
    personagens = [
        PersonagemMarvel("Groot", "Guardiões da Galáxia", "Resistência e controle de grupo", 700),
        PersonagemMarvel("Rocket Raccoon", "Guardiões da Galáxia", "Alto dano por segundo", 250)
    ]

    personagens[0].habilidades.extend(["Crescimento de Raízes", "Escudo de Galhos"])
    personagens[0].adicionar_item_inventario("Galho Protetor", "Defensivo", "Reduz dano em 60% por 7 segundos")

    personagens[1].habilidades.extend(["Canhão de Plasma", "Granada de Gravidade"])
    personagens[1].adicionar_item_inventario("Granada de Fragmentação", "Explosivo", "Causa 150 de dano em área")

    print("Escolha seu personagem:")
    for i, p in enumerate(personagens):
        print(f"{i + 1}. {p.nome} ({p.poder_principal})")

    while True:
        escolha = input("Digite o número do personagem: ")
        if escolha in ["1", "2"]:
            jogador = personagens[int(escolha) - 1]
            inimigo = personagens[1] if jogador == personagens[0] else personagens[0]
            return jogador, inimigo
        else:
            print("Escolha inválida. Tente novamente.")

def turno(jogador, inimigo):
    print("\nSeu turno!")
    print("1. Atacar")
    print("2. Defender")
    print("3. Desistir")

    acao = input("Escolha uma ação: ")

    if acao == "1":
        print("\nEscolha uma habilidade:")
        for i, h in enumerate(jogador.habilidades):
            print(f"{i + 1}. {h}")
        h_escolhida = input("Digite o número da habilidade: ")
        if h_escolhida.isdigit() and 1 <= int(h_escolhida) <= len(jogador.habilidades):
            habilidade = jogador.habilidades[int(h_escolhida) - 1]
            dano = random.randint(50, 150)
            if inimigo.defendendo:
                dano = int(dano * 0.4)
                inimigo.defendendo = False
            inimigo.vida -= dano
            print()
            jogador.usar_habilidade(habilidade, inimigo)
            print(f"{inimigo.nome} recebeu {dano} de dano!")
        else:
            print("Habilidade inválida.")
    elif acao == "2":
        jogador.defendendo = True
        print(f"{jogador.nome} está defendendo e tomará menos dano no próximo turno.")
    elif acao == "3":
        print("Você desistiu. Fim de jogo.")
        exit()
    else:
        print("Ação inválida.")

def turno_inimigo(inimigo, jogador):
    print(f"\nTurno do inimigo: {inimigo.nome}")
    acao = random.choice(["atacar", "defender"])

    if acao == "atacar":
        habilidade = random.choice(inimigo.habilidades)
        dano = random.randint(50, 150)
        if jogador.defendendo:
            dano = int(dano * 0.4)
            jogador.defendendo = False
        jogador.vida -= dano
        inimigo.usar_habilidade(habilidade, jogador)
        print(f"{jogador.nome} recebeu {dano} de dano!")
    else:
        inimigo.defendendo = True
        print(f"{inimigo.nome} está defendendo.")

def combate():
    jogador, inimigo = escolher_personagem()
    print("\nBATALHA INICIADA!\n")

    while jogador.vida > 0 and inimigo.vida > 0:
        print("\n🧍 Seu Personagem")
        jogador.resumo()
        print("\n👾 Inimigo")
        inimigo.resumo()

        turno(jogador, inimigo)
        if inimigo.vida <= 0:
            print(f"\n{inimigo.nome} foi derrotado! Você venceu!")
            break

        turno_inimigo(inimigo, jogador)
        if jogador.vida <= 0:
            print(f"\n{jogador.nome} foi derrotado! Você perdeu!")
            break

if __name__ == "__main__":
    combate()
