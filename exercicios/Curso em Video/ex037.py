num = int(input('Digite um numero: '))
met = int(input('Escolha como você prentende visualizar o numero {}\n [1]Binario\n [2]Octal\n [3]Hexadecimal\n Digite: '.format(num)))
if met == 1:
    num = bin(num)
    print('Seu numero em binário será: {}'.format(num[2:]))
elif met == 2:
    num = oct(num)
    print('Seu numero em octal será: {}'.format(num[2:]))
elif met == 3:
    num = hex(num)
    print('Seu numero em hexadecimal será: {}'.format(num))
else:
    print('valor inserido é invalido')
