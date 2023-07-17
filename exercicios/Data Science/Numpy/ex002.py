import numpy as np

np.pi
np.inf
np.nan


matriz = np.matrix([1,2,3])
variosUm = np.ones(9)
print(matriz)

a_1 = np.ones(5)
a_2 = np.ones(5)


print(variosUm.reshape(3,3))
print(variosUm.reshape(3,3))


arrayVertical = np.vstack((a_1, a_2))
arrayHorizontal = np.hstack((a_1, a_2))

print(arrayVertical)
print(arrayHorizontal)

eye = np.eye(10)
eye = eye *9
print(eye)

print(variosUm)