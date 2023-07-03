velo = int(input('Qual sua velocidade na via? '))
if velo >= 80:
    placa = (velo - 80) * 7
    print('voce excedeu os limites de velocidade da via!')
    print('sera atribuido um valor de R${} como multa'.format(placa))
else:
    print('sua velocidade está dentro dos conformes')
