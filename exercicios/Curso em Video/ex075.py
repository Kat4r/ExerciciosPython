soma = c = numpar = 0
tuplakkk = []
pares = []
for i in range(0,4):
    num = int(input('Digite um numero: '))
    tuplakkk.append(num)
tuplakkk = tuple(tuplakkk)

for numeros in tuplakkk:
    if numeros == 9:
        c += 1
    if numeros % 2 == 0:
        pares.append(numeros)

if 9 in tuplakkk:
    print('o numero 9 apareceu \033[31m{}\033[m vezes'.format(c))
if 3 in tuplakkk:
    print('o numero 3 apareceu a primeira vez em \033[31m{}\033[m'.format(tuplakkk.index(3)+1))
if pares:
    print('Os numeros pares foram: \033[32m{}'.format(', '.join(map(str, pares))))








