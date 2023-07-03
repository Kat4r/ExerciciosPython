import random

c = 0

jogadores = {'Jogador 1':random.randint(1,6),
             'Jogador 2':random.randint(1,6),
             'Jogador 3':random.randint(1,6),
             'Jogador 4':random.randint(1,6)}

for jogador,dado in jogadores.items():
    print(f"o {jogador} tirou {dado} no dado")

vencedores = sorted(jogadores.items(), key=lambda x:x[1], reverse=True)
ranking = dict(vencedores)


print("\033[7:48m-="*9, "Ranking", '=-'*9,'\033[m\n\033[7:48m-=          Tabela de vencedores           =-\033[m')
print("\033[7:48m-="*22, end='-\033[m')
print()

while c < len(jogadores):
    for vencedor,dado in ranking.items():
        c += 1
        if c == 1:
            print(f"\n{vencedor} foi o vencedor por ter tirado {dado} no dado")
        else:
            print(f"{vencedor} tirou {dado} no dado")

