import random
computador = random.randrange(10)
contar = 1
player = int(input('Digite um numero de 0 a 10: '))
while player != computador:
    contar = contar + 1
    if player < computador:
        print('voce ta quase la, um pouco \033[32mmais\033[m!')
    else:
        print('voce ta quase la, um pouco \033[31mmenos\033[m!')
    player = int(input('Quase la, tente novamente: '))
if contar == 1:
    print('\033[1:32mPARABENS!! Você conseguiu superar o computador de primeira!')
else:
    print('\033[1:32mParabens!\033[m você conseguiu derrotar o computador após \033[1:33m{}\033[m tentativas'.format(contar))





