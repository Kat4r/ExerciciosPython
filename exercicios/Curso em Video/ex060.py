import numpy

num = int(input('Digite um numero: '))
calc = []
for i in range(num,1,-1):
    print(i, 'x ', end='')
    calc.append(i)
print('1 =',numpy.prod(calc))

###################################

import math
num = int(input('Digite um numero: '))
num2 = math.factorial(num)
print('o fatorial de {}! é {}'.format(num,num2))

###################################

num = int(input('Digite um numero: '))
num_lista = []
soma = 1
for i in range(num,1,-1):
    num_lista.append(i)
for numeros in num_lista:
    print(numeros, 'x ', end='')
    soma = soma * numeros
print('1 =',soma)

###################################

num = int(input('Digite um numero: ')) + 1
numeros = []
import numpy
while num >= 2:
    num = num - 1
    if num > 1:
        print(num,'x ', end='')
    else:
        print(num,'= ', end='')
    numeros.append(num)
print(numpy.prod(numeros))


