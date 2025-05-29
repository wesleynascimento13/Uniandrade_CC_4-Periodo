from itens import Pocao, Arma, Armadura

def main():
    cura = Pocao("Vida eterna")
    (cura.usar())

    faca = Arma("Tramontina")
    (faca.usar())

    escudo = Armadura("Escudo Ouro")
    (escudo.usar())

if __name__ == "__main__":
    main()
