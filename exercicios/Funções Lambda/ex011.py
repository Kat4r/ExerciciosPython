from random import  randint

numeros = [randint(0,50) for i in range(25)]

maior = lambda lista: max(lista)

print(maior(numeros))
