from random import  randint

numeros = [randint(0,50) for i in range(25)]

menor = lambda lista: min(lista)

print(menor(numeros))
