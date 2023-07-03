num = int(input('digite um numero para verificarmos se ele é primo: '))
while num <= 1:
    print('\033[31mO numero \033[32m1\033[m \033[31mnão compõe e nem se constitui um numero PRIMO')
    num = int(input('Tente novamente: '))
multiplo = c = 0

print('\033[32m', 1, '\033[m', end= '')
for num_pr in range(2,num):
    if num % num_pr == 0:
        c += 1
        multiplo += 1
        print(f'\033[32m{num_pr}\033[m', end='')
    else:
        print(f'\033[31m{num_pr}\033[m', end='')
print('\033[32m', num, '\033[m')
if multiplo != 0:
    print('\no numero informado \033[1:31mnão é primo\033[m pois pode ser divido até \033[34m{}\033[m vezes'.format(c+2))
else:
    print('\n\033[1:33mo numero informado é primo pois foi dividido somente 2 vezes\033[m')





