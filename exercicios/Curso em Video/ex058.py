import time
loop = True
num1 = float(input('\033[32mDigite o primeiro numero:\033[m '))
num2 = float(input('\033[32mDigite o segundo numero:\033[m '))
while loop == True:
    soma = 0
    print('Digite um valor correspondente ao seu interesse:\n'
              '\033[34m[ 0 ] \033[4:37mSoma\033[m\n'
              '\033[34m[ 1 ] \033[4:37mSubtração\033[m\n'
              '\033[34m[ 2 ] \033[4:37mMultiplicação\033[m\n'
              '\033[34m[ 3 ] \033[4:37mDivisão\033[m\n'
              '\033[34m[ 4 ] \033[4:37mNovos numeros\033[m\n'
              '\033[34m[ 5 ] \033[4:37mQual o maior\033[m\n'
              '\033[34m[ 6 ] \033[4:31mSair do programa\033[m\n')
    opt = int(input('Informe a opção (somente numeros): '))
    print('Processando...')
    time.sleep(1.5)
    while opt >=7 or opt < 0:
        print('\033[31mNumero incorreto!\033[m')
        opt = int(input('Informe a opção (somente numeros): '))
    if opt == 0:
        soma = num1 + num2
        print('Soma entre os numeros escolhidos é {}'.format(soma))
    elif opt == 1:
        soma = num1 - num2
        print('A subtração entre os numeros escolhidos é {}'.format(soma))
    elif opt == 2:
        soma = num1 * num2
        print('A multiplicação entre os numeros escolhidos é {}'.format(soma))
    elif opt == 3:
        soma = num1 / num2
        print('A divisão entre os numeros escolhidos é {:.2f}'.format(soma))
    elif opt == 4:
        num1 = float(input('\033[32mDigite o primeiro numero:\033[m '))
        num2 = float(input('\033[32mDigite o segundo numero:\033[m '))
    elif opt == 5:
        if num1 > num2:
            print('O numerio maior é {}'.format(num1))
        else:
            print('O numerio maior é {}'.format(num2))
    else:
        print('O programa será finalizado...')
        break

