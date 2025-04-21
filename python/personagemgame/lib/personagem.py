class PersonagemMarvel:
    def __init__(self, nome, afiliacao, poder_principal, vida):
        self.nome = nome
        self.afiliacao = afiliacao
        self.poder_principal = poder_principal
        self.vida = vida
        self.habilidades = []
        self.inventario = []
        self.defendendo = False
        self.vida_maxima = vida

    def usar_habilidade(self, habilidade, alvo):
        print(f"{self.nome} utilizou '{habilidade}' contra {alvo.nome}!")

    def adicionar_item_inventario(self, nome, tipo, efeito):
        item = {"nome": nome, "tipo": tipo, "efeito": efeito}
        self.inventario.append(item)

    def barra_de_vida(self):
        total_blocos = 20
        vida_ratio = max(self.vida, 0) / self.vida_maxima
        preenchido = int(vida_ratio * total_blocos)
        return "█" * preenchido + "░" * (total_blocos - preenchido)

    def resumo(self, titulo=""):
        inv = self.inventario[0]
        print(f"{titulo}: {self.nome} | Vida: {self.vida} {self.barra_de_vida()}")
        print(f"Afiliação: {self.afiliacao}")
        print(f"Poder Principal: {self.poder_principal}")
        print(f"Habilidades: {', '.join(self.habilidades)}")
        print(f"Inventário: {inv['nome']} ({inv['tipo']}) - {inv['efeito']}")
        print("-" * 40)
