import random
import time
from datetime import datetime
from exercicios.SQL import sqlpy

coneccao = sqlpy.conectar('localhost', 'root', 'root')



def diaHojeSQL():
    dia = datetime.now().day
    mes = datetime.now().month
    ano = datetime.now().year
    return f"{ano}-{mes}-{dia}"

pontos = 0
mao = ('pedra', 'papel', 'tesoura')
jogo = ''


while jogo != 'O Computador vence!':
    player = int(input('Escolha um dos itens para poder jogar!\n'
                   '\033[1:32m[ 0 ] Pedra\n'
                   '\033[1:32m[ 1 ] Papel\n'
                   '\033[1:32m[ 2 ] Tesoura\033[m\n'
                   '\033[4mDigite sua escolha:\033[m '))
    while player >= 3 or player < 0:
        print('\033[31mescolha incorreta!\033[m')
        player = int(input('Tente numeros \033[1:33mSOMENTE\033[m de 0 a 2: '))

    if player == 0:
        player = mao[0]
    elif player == 1:
        player = mao[1]
    elif player == 2:
        player = mao[2]
    computador = random.randint(0, 2)
    print('JO')
    time.sleep(.50)
    print('KEN')
    time.sleep(.50)
    print('PO!')
    time.sleep(0.25)
    if computador == 0:
        if player == mao[0]:
            jogo = 'Empate!'
        elif player == mao[1]:
            jogo = 'O Jogador vence!'
            pontos += 1
        elif player == mao[2]:
            jogo = 'O Computador vence!'
    elif computador == 1:
        if player == mao[0]:
            jogo = 'O Computador vence!'
        elif player == mao[1]:
            jogo = 'Empate!'
        elif player == mao[2]:
            jogo = 'O Jogador vence!'
            pontos += 1
    elif computador == 2:
        if player == mao[0]:
            jogo = 'O Jogador vence!'
            pontos += 1
        elif player == mao[1]:
            jogo = 'O Computador vence!'
        elif player == mao[2]:
            jogo = 'Empate!'


    print('\033[7:38m~~' * 18, '\033[m')
    print('\033[7:38m=-' * 7, player, '-=' * 7, '\033[32m[Jogador]\033[m')
    print('\033[7:38m=-' * 7, mao[computador], '-=' * 7, '\033[31m[Computador]\033[m')
    print('\033[7:38m~~' * 18, '\033[m')
    print(f'\033[36m{jogo}\033[m\n')

print(f"Você fez {pontos} pontos!!")
nome = input("Digite seu nome [MAX 3 LETRAS]: ")
while len(nome) != 3:
    nome = input("Digite seu nome [MAX 3 LETRAS]: ")

sqlpy.executarQuery(coneccao, 'use pontos')

query = 'insert into pontuacao values(default,"{}", "{}","{}")'.format(nome.upper(),diaHojeSQL(),pontos)
sqlpy.executarQuery(coneccao, query)