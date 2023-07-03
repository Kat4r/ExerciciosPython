import math
c1 = float(input('digite o tamanho do cateto'))
c2 = float(input('digite o tamanho do segundo cateto'))
soma = (c1 * c1) + (c2 * c2)
raiz = math.sqrt(soma)
print('de acordo com os dados informados, a hipotenusa é {:.2f}'.format(raiz))
