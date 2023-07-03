import time
anoatual = int(input('digite um ano: '))
data = time.localtime()
if anoatual == 0:
    print('Estamos em {} e não é um ano bissexto'.format(time.strftime('%Y', data)))
elif anoatual % 400 == 0 or anoatual % 100 != 0 and anoatual % 4 == 0:
    print('o ano de {} é bissexto'.format(anoatual))
else:
    print('o ano de {} não é bissexto'.format(anoatual))
