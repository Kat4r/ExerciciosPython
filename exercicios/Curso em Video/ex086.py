matriz = [[],[],[],
         [],[],[],
         [],[],[]]
c = m1 = m2 = 0

for i in range(len(matriz)):
    matriz[i] = int(input('digite um valor para [{},{}]: '.format(m2,m1)))
    m1 = m1 + 1
    if m1  > 2:
        m1 = 0
        m2 += 1

maxValor = max(matriz)
maxDigitos = len(str(maxValor))

for i in matriz:
    print("[ {:^{}} ]".format(i,maxDigitos), end='')
    c +=1
    if c == 3:
        print()
        c = 0

