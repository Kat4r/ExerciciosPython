import random
loop = True
contador = 0
while loop == True:
    computador = random.randint(0,10)
    player_mao = input('PAR ou IMPAR [P/I]: ').upper()[0]
    while not player_mao.isalpha() or player_mao not in ['P', 'I']:
        player_mao = input('Digite apenas P ou I: ').upper()
    while player_mao != 'P' and player_mao != 'I':
        player_mao = str(input('Digite APENAS P ou I: ').upper())[0]
    player_num = int(input('Escolha um numero de 0 a 10: '))
    while player_num < 0 or player_num > 10:
        player_num = int(input("São aceitos somente numeros de 0 até 10!: "))
    jogo = computador + player_num
    resultado = 0
    if player_mao == 'P':
        if jogo % 2 == 0:
            contador = contador + 1
            resultado = 'O Jogador venceu!'
        else:
            resultado = 'O Computador venceu!'
            loop = False

    elif player_mao == 'I':
        if jogo % 2 != 0 and jogo % 3 == 0:
            contador = contador + 1
            resultado = 'O jogador venceu!'
        else:
            resultado = 'O Computador venceu!'
            loop = False
    print('\n' * 10)
    print('~'*60)
    print('computador jogou {} e o Player jogou {}, dando um total de {}'.format(computador,player_num,jogo))
    print('Portando, {}'.format(resultado))
    print('~'*60)
    if resultado == 'O Computador venceu!':
        print('O jogador perdeu após {} vitórias'.format(contador))


