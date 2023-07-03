jogador = {}
jogos = []

jogador['nome'] = input("Digite o nome do jogador: ").title().strip()
jogador['partidas'] = int(input(f'quantas partidas o \033[34m{jogador["nome"]}\033[m jogou?: '))

for i in range(jogador['partidas']):
    jogos.append(int(input(f"Quantos gols ele marcou na {i+1}º partida? ")))

print("\n\033[4:32m" ,"-=" * 13, "MURAL", '=-' *13, "\033[m \n")
print(f"O jogador \033[34m{jogador['nome']}\033[m fez \033[32m{sum(jogos)}\033[m gols na carreira\n")
for pos, gol in enumerate(jogos):
    print(f"    -> na partida {pos+1} {jogador['nome']} fez {gol} gols")
