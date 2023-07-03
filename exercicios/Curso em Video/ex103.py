def ficha(nome,gols):
    if not nome:
        nome = "<desconhecido>"
    if not gols or not gols.isdigit():
        gols = 0

    frase = f" O jogador {nome} fez {gols} no campeonato "
    print("-"* int(len(frase)+2))
    print(frase)
    print("-" * int(len(frase)+2))


ficha(input("digite o nome do jogador"), input("Digite os gols"))
