import numpy as np

lista1 = np.arange(1,10,1)
lista2 = lista1.copy()

lista1.argmax()
lista1.sum()
lista1.cumsum()

lista1[4] = 4

print(lista1)
print(lista2)