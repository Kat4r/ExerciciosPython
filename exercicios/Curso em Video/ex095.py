import random
from modulos.libtestes import testespy as tpy
from exercicios.SQL import  sqlpy as sql

jogador = {}
jogos, estatisticas = [], []
dados = escolha = None
coneccao = sql.conectar('localhost', 'root', 'root')
sql.executarQuery(coneccao, 'use jennaortega')

while dados != "n":

    jogador = {}
    jogos.clear()

    jogador['Nome'] = nomeAgora =  tpy.nomesJogadoresRand()
    #jogador['Nome'] = input("Digite o nome do jogador: ").title().strip()
    jogador['Partidas'] = partidaAgora = random.randint(1,6)

    #jogador['partidas'] = int(input(f'quantas partidas o \033[34m{jogador["nome"]}\033[m jogou?: '))

    for i in range(jogador['Partidas']):
        jogos.append(random.randint(0,5))
        #jogos.append(int(input(f"Quantos gols ele marcou na {i+1}º partida? ")))
    jogador['Gols'] = jogos[:]
    jogador['Total de gols'] = golsAgora = sum(jogos)

    sql.executarQuery(coneccao, f'insert into cristianoronaldo values(default, "{golsAgora}", "{nomeAgora}", "{partidaAgora}")')
    dados = input("Deseja continuar?: ").lower()[0]
    estatisticas.append(jogador)



print("\n\033[4:32m" ,"-=" * 13, "MURAL", '=-' *13, "\033[m \n")

for pos, dadosjogador in enumerate(estatisticas):
    print(f"======= {pos+1}ºJogador ======")
    for k,v in dadosjogador.items():
        if k != 'Gols':
            print(f"{k}: \033[34m{v}\033[m")
    print()

while True:
    try:
        escolha = int(input("Deseja saber as informações de qual jogador? \033[31m[ 0 ]\033[m para encerrar: "))-1
        if escolha < 0:
            exit()
        print(f"\nO jogador \033[34m{estatisticas[escolha]['Nome']}\033[m fez "
              f"\033[32m{estatisticas[escolha]['Total de gols']}\033[m gols na carreira\n")

        for pos, gol in enumerate("".join(map(str, estatisticas[escolha]['Gols']))):
            print(f"    -> na partida {pos+1} o \033[34m{estatisticas[escolha]['Nome']}\033[m fez \033[32m{gol} gols\033[m")
        print()




    except Exception as erro:
        print(erro)
        print("\n\033[1:31mO numero informado está além dos limites da lista\033[m\n")








