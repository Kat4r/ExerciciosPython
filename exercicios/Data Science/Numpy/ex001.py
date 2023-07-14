import numpy as np

vetorUnidimensional = np.array([1,2,3])

vetorBidimensional = np.array([[1,2,3],[4,5,6]])

vetorTridimensional = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

vetorRange = np.arange(1,20,3)

print(vetorTridimensional.ndim)
print(vetorTridimensional.shape)
print(vetorTridimensional.size)

vetorRange[0] = 5

print(vetorRange)