import numpy as np

np.pi
np.inf
np.nan
#Valores para uso comum em numpy

matriz = np.matrix([1,2,3]) #gera uma matriz
variosUm = np.ones(9) #gera um vetor preenchido de numeros 1
print(matriz)

a_1 = np.ones(5)
a_2 = np.ones(5)


print(variosUm.reshape(3,3)) #rearranja o array para uma nova forma considerando LINHA / COLUNA
print(variosUm.reshape(3,3)) #faz a mesma coisa, porem agora altera DIRETAMENTE o objeto array


arrayVertical = np.vstack((a_1, a_2)) #alinha os arrays em forma vertical (os arrays precisam ter o exato mesmo tamanho em colunas)
arrayHorizontal = np.hstack((a_1, a_2)) #alinha os arrays em forma vertical (os arrays precisam ter o exato mesmo tamanho em linhas)

print(arrayVertical)
print(arrayHorizontal)

eye = np.eye(10) #gera um array diagonal de acordo com o valor
eye = eye *9
print(eye)

print(variosUm)