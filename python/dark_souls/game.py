from jogadores.cavaleiro import Cavaleiro
from itens.pocao import Pocao
from inimigos.chefe import Chefe

def barra_de_vida(valor_atual, valor_maximo, largura=20, cor=''):
    proporcao = valor_atual / valor_maximo
    preenchido = int(proporcao * largura)
    vazio = largura - preenchido
    barra = '█' * preenchido + '░' * vazio
    return f"{cor}[{barra}] {valor_atual}/{valor_maximo}\033[0m"

def main():
    cavaleiro = Cavaleiro("Rei Artur", 20)
    chefe = Chefe("Senhor das Cinzas", 30)
    pocao = Pocao("Poção de Vida", 25)

    while True:
        print()
        print("Vida do Chefe:    ", barra_de_vida(chefe.saude, 400, cor='\033[91m'))
        print("Vida do Cavaleiro:", barra_de_vida(cavaleiro.saude, 100, cor='\033[92m'))
        print("--- MENU ---")
        print("1. Atacar Chefe")
        print("2. Defender")
        print("3. Usar Poção")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cavaleiro.atacar()
            chefe.saude = -cavaleiro.dano
            if chefe.saude > 0:
                dano = chefe.atacar()
                cavaleiro.saude = -dano
        elif opcao == "2":
            cavaleiro.defender()
            print("Chefe não atacou desta vez.")
        elif opcao == "3":
            pocao.usar(cavaleiro)
        elif opcao == "4":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida.")

        if cavaleiro.saude <= 0:
            print("Você foi derrotado!")
            break
        if chefe.saude <= 0:
            print("Você venceu o chefe!")
            break

if __name__ == '__main__':
    main()
