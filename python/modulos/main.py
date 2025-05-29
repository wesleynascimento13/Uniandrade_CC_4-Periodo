import player
from player import atacar, dados
from player import *  # importe tudo

def main():
    atacar()
    dados()
    player.atacar()
    player.dados()

if __name__ == "__main__":
    main()
    print("Eu sou o main")
    print(__name__)
