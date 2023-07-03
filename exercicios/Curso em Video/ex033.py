n1 = int(input('DIgite um numero: '))
n2 = int(input('DIgite outro numero: '))
n3 = int(input('DIgite outro numero: '))
if n1 > n2 and n1 > n3:
    print('o numero {} é o maior '.format(n1))
elif n2 > n3 and n2 > n1:
    print('o numero {} é o maior '.format(n2))
else:
    print('o numero {} é o maior '.format(n3))
if n1 < n2 and n1 < n3:
    print('o numero {} é o menor '.format(n1))
elif n2 < n3 and n2 < n1:
    print('o numero {} é o menor '.format(n2))
else:
    print('o numero {} é o menor '.format(n3))
