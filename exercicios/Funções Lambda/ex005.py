lista = list(range(1,51))

numpar = lambda lista: [num for num in lista if num % 2 == 0]
print(numpar(lista))

def numpar(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares
print(numpar(lista))


