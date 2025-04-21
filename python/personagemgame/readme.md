# 🦸 Projeto Marvel Rivals em Python

Este projeto foi desenvolvido em **Python no Codespaces**, inspirado no jogo **Marvel Rivals**. Ele simula dois personagens interativos — Groot e Rocket Raccoon — que podem ser visualizados ou colocados para batalhar em um sistema de combate por turnos no terminal.

## 📦 Estrutura do Projeto

python/
├── lib/
│   ├── personagem.py         # Classe PersonagemMarvel
│   └── inventario.py         # Funções para gerenciar o inventário
├── src/
│   ├── personagem_game.py    # Exibe dados dos personagens
│   └── batalha.py            # Sistema de combate interativo

## 🔧 Classe PersonagemMarvel

A classe `PersonagemMarvel`, localizada em `lib/personagem.py`, possui os seguintes atributos:

- `nome`
- `afiliacao`
- `poder_principal`
- `vida`
- `habilidades` (lista)
- `inventario` (lista de dicionários com nome, tipo e efeito)

**Métodos:**

- `usar_habilidade`
- `adicionar_item_inventario`
- `status`
- `barra_de_vida`
- `resumo`

## 👤 `personagem_game.py` — CUMPRE OS REQUISITOS DA ATIVIDADE

Este é o script **principal exigido pela atividade**. Ele instância dois personagens diferentes:

- **Groot**: 700 de vida, foco em resistência  
- **Rocket Raccoon**: 250 de vida, foco em dano rápido  

Ambos possuem habilidades e itens. Ao executar o script, ele imprime no terminal:

- Nome, afiliação e poder principal  
- Vida (com barra visual)  
- Habilidades e inventário formatados  

> Este código atende exatamente ao que foi solicitado: definição de classe, atributos, métodos, uso de estruturas de dados, criação de personagens e impressão dos dados.

## ⚔️ `batalha.py` — CÓDIGO EXTRA (COMPLEMENTAR E EXPANDIDO)

Este script foi criado **apenas para expandir e complementar o que foi feito em `personagem_game.py`**. Ele adiciona uma mecânica de combate interativo que permite:

- Escolher um personagem
- Realizar turnos de ataque, defesa ou desistência
- Ver barra de vida se atualizando dinamicamente
- Enfrentar o outro personagem com IA simples
- Finalizar o jogo com vitória, derrota ou desistência

## ▶️ Como Executar

Abra o terminal na pasta `python/` e execute os comandos abaixo:

### Para rodar o que foi pedido na atividade:

```bash
python3 src/personagem_game.py
```

### Para rodar o código extra com modo de batalha:

```bash
python3 src/batalha.py
```
## ✍️ Autor

Trabalho individual — **Wesley Vilgino do Nascimento**  
Curso: Ciência da Computação — Uniandrade  
Período: 4º Semestre | Ano: 2025
