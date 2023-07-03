import random as r
cores = ['\033[31m', '\033[32m','\033[33m','\033[34m','\033[35m','\033[36m','\033[37m',]
num = int(input('Digite um numero para ser feita a tabuada: '))
if num <=0:
    print('\033[1:31m-----Fim-----\033[m')
    exit()
while True:
    c = 1
    resultado = 0
    while True:
        resultado = num * c
        print(r.choice(cores),'| {} x {} = {} |'.format(num,c,resultado))
        c = c + 1
        if c > 10:
            break
    num = int(input('\033[mDigite outro numero para ser feita a tabuada: '))
    if num <=0:
        break
print('\033[1:31m-----Fim-----\033[m')



