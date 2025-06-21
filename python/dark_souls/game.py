from jogadores.cavaleiro import Cavaleiro
from itens.pocao import Pocao
from inimigos.chefe import Chefe
from inimigos.morto_vivo import MortoVivo
import random
from random import sample

def barra_de_vida(valor_atual, valor_maximo, largura=20, cor=''):
    proporcao = valor_atual / valor_maximo
    preenchido = int(proporcao * largura)
    vazio = largura - preenchido
    barra = '█' * preenchido + '░' * vazio
    return f"{cor}[{barra}] {valor_atual}/{valor_maximo}\033[0m"

def escolher_inimigo():
    print("\n--- ESCOLHA SEU DESAFIO ---")
    print("1. Chefe: Senhor das Cinzas")
    print("2. Morto-Vivo (inimigo aleatório)")
    escolha = input("Digite o número do inimigo: ")

    if escolha == "1":
        inimigo = Chefe("Senhor das Cinzas", 30)
        vida_maxima = 200
    elif escolha == "2":
        mortos_vivos = [
            {
                "nome": "Esqueleto Sombrio",
                "dano": 25,
                "saude": 120,
                "ataques": [
                    {"nome": "Mordida Enferrujada", "bonus": 5},
                    {"nome": "Arranhão Maldito", "bonus": 10},
                    {"nome": "Grito Espectral", "bonus": 0}
                ]
            },
            {
                "nome": "Carniçal Rastejante",
                "dano": 20,
                "saude": 110,
                "ataques": [
                    {"nome": "Investida Podre", "bonus": 15},
                    {"nome": "Lambida Tóxica", "bonus": 5},
                    {"nome": "Esfarrapar", "bonus": 10}
                ]
            },
            {
                "nome": "Zumbi Selvagem",
                "dano": 30,
                "saude": 100,
                "ataques": [
                    {"nome": "Cabeçada Podre", "bonus": 0},
                    {"nome": "Mordida Fúria", "bonus": 10},
                    {"nome": "Empurrão Descontrolado", "bonus": 5}
                ]
            },
            {
                "nome": "Sombra Cadavérica",
                "dano": 22,
                "saude": 130,
                "ataques": [
                    {"nome": "Garras Etéreas", "bonus": 8},
                    {"nome": "Sopro do Túmulo", "bonus": 4},
                    {"nome": "Toque Gélido", "bonus": 6}
                ]
            }
        ]
        selecionado = random.choice(mortos_vivos)
        inimigo = MortoVivo(
            nome=selecionado["nome"],
            dano=selecionado["dano"],
            saude=selecionado["saude"],
            ataques=selecionado["ataques"]
        )
        vida_maxima = selecionado["saude"]
    else:
        print("Opção inválida. Iniciando contra o Chefe por padrão.")
        inimigo = Chefe("Senhor das Cinzas", 30)
        vida_maxima = 200

    return inimigo, vida_maxima

def main():
    cavaleiro = Cavaleiro("Rei Artur", 20)
    inimigo, vida_inimigo_max = escolher_inimigo()
    cavaleiro.especial = 0

    possiveis_pocoes = [
        Pocao("Poção Fraca", 20, 2),
        Pocao("Poção Média", 40, 1),
        Pocao("Poção Forte", 60, 1),
        Pocao("Poção Vital", 80, 1),
        Pocao("Poção Suprema", 100, 1)
    ]

    inventario = sample(possiveis_pocoes, k=3)

    while True:
        print()
        print(f"Vida de {inimigo.nome}: ", barra_de_vida(inimigo.saude, vida_inimigo_max, cor='\033[91m'))
        print("Vida do Cavaleiro:", barra_de_vida(cavaleiro.saude, 100, cor='\033[92m'))
        print("Especial:         ", barra_de_vida(cavaleiro.especial, 100, cor='\033[96m'))
        print("--- MENU ---")
        print("1. Atacar Inimigo")
        print("2. Defender")
        print("3. Inventário")
        print("4. Sair")
        if cavaleiro.especial >= 100:
            print("5. ATAQUE ESPECIAL DISPONÍVEL")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cavaleiro.atacar()
            inimigo.saude = -cavaleiro.dano
            cavaleiro.especial = min(100, cavaleiro.especial + 20)
            if inimigo.saude > 0:
                dano = inimigo.atacar()
                cavaleiro.saude = -dano
        elif opcao == "2":
            cavaleiro.defender()
            if hasattr(inimigo, 'prever_ataque'):
                inimigo.prever_ataque()
            else:
                print(f"{inimigo.nome} parece preparar um ataque maligno...")
        elif opcao == "3":
            print("\n--- INVENTÁRIO DE POÇÕES ---")
            for i, pocao in enumerate(inventario):
                print(f"{i + 1}. {pocao.nome} (+{pocao.cura}) - Quantidade: {pocao.quantidade}")
            escolha = input("Digite o número da poção para usar ou Enter para cancelar: ")
            if escolha.isdigit():
                idx = int(escolha) - 1
                if 0 <= idx < len(inventario):
                    inventario[idx].usar(cavaleiro)
                    if inventario[idx].quantidade == 0:
                        inventario.pop(idx)
                else:
                    print("Opção inválida.")
        elif opcao == "4":
            print("Saindo do jogo...")
            break
        elif opcao == "5" and cavaleiro.especial >= 100:
            print("ATAQUE ESPECIAL ATIVADO!")
            inimigo.saude = -cavaleiro.dano * 2
            cavaleiro.especial = 0
            if inimigo.saude > 0:
                dano = inimigo.atacar()
                cavaleiro.saude = -dano
        else:
            print("Opção inválida.")

        if cavaleiro.saude <= 0:
            print("Você foi derrotado!")
            break
        if inimigo.saude <= 0:
            print(f"Você venceu {inimigo.nome}!")
            break

if __name__ == '__main__':
    main()
