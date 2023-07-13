import numpy as np

lista1 = np.arange(1,10,1)
lista2 = lista1.copy()

lista1.argmax() #argmin, retorna a posição de onde estiver o indice de maior/menor valor
lista1.sum() #mean, std. Assim como em pandas, retorna soma, media, desvio etc
lista1.cumsum() #cumprod, retorna a soma cumulativa ou o produto cumulativo

lista1[4] = 4

print(lista1)
print(lista2)