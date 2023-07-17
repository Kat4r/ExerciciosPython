import numpy as np

lista = np.arange(6).reshape(2,3)**5

print(lista[::2])
print(lista[:32])
print(lista[1:5])

#assim como strings, o metodo de tratamento de arrays é identico, representando separações por " : " e considerando "start, stop, step"

