dd = int(input('digite o dia: '))
mm = int(input('digite o mes: '))
aa = int(input('digite o ano: '))
if dd <= 31 and mm <= 12 and aa <= 9999:
    print('Os numeros informados são validos para Dia/Mes/Ano \nA data informada representa: {}/{}/{}'.format(dd, mm, aa))
else:
    print('digite novamente')