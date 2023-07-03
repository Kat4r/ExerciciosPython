from random import randint

numeros = [randint(0,100) for i in range(25)]

numeros10 = lambda lista: [num for num in lista if num >= 30]

print(numeros10(numeros))