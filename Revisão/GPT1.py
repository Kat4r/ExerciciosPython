import random


numeros = []
for i in range(1,51):
    numero = random.randint(0,100)
    numeros.append(numero)

numparimpar = [[],[]]
for numero in numeros:
    if numero % 2 == 0:
        numparimpar[0].append(numero)
    else:
        numparimpar[1].append(numero)

print(f'na lista gerada, os seguintes numeros são pares: {sorted(numparimpar[0])}\n'
      f'e os seguintes são impares: {sorted(numparimpar[1])}')

