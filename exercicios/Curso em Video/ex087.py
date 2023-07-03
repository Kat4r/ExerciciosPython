import math
from math import *


matriz = [[],[],[],
         [],[],[],
         [],[],[]]
pares, columns = [],[]

c = m1 = m2 = linha = soma = 0

for i in range(len(matriz)):
    matriz[i] = int(input('digite um valor para [{},{}]: '.format(m2,m1)))
    linha += 1

    if linha <= 3:
        columns.append(matriz[i])

    if linha >= 4 and linha <= 6:
        soma = soma + matriz[i]

    m1 = m1 + 1
    if m1  > 2:
        m1 = 0
        m2 += 1

maxValor = max(matriz)
maxDigitos = len(str(maxValor))

for num in matriz:
    if num % 2 == 0:
        pares.append(num)

print()

for i in matriz:
    print("\033[34m[ \033[32m{:^{}}\033[m \033[34m]".format(i,maxDigitos), end='')
    c +=1
    if c == 3:
        print()
        c = 0
print()

print('\033[mA soma de todos os pares dessa matriz é \033[31m{}'.format(sum(pares)))
print('\033[mA soma dos valores na segunda linha é \033[31m{}'.format(soma))
print('\033[mO maior valor na terceira coluna é \033[31m{}'.format(max(columns)))