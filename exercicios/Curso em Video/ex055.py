import numpy
pessoas = []
for peso in range(5):
    pessoa = float(input('Digite um peso: '))
    pessoas.append(pessoa)
pessoas = numpy.sort(pessoas)
print('A pessoa mais leve pesa {:.1f} Kg'.format(pessoas[0]))
print('A pessoa mais pesada pesa {:.1f} Kg'.format(pessoas[-1]))
