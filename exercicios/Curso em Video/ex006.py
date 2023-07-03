n = int(input('digite um numero: '))
d = n * 2
t = n * 3
raiz = n ** (1/2)
print('O dobre equivale a \033[1;34;40m{}\033[m\n'
      'O triplo equivale a \033[1;32;40m{}\033[m\n'
      'E sua raiz quadrada é \033[4;35;40m{:.2f}\033[m'.format(d,t,raiz))