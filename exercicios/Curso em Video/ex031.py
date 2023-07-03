viagem = float(input('digite a distancia de sua viagem R$: '))
dist = viagem * 0.50
if viagem >= 200:
    dist = viagem * 0.45
    print('Sua viagem ficará por R${:.2f} por conta do desconto'.format(dist))
else:
    print('Sua viagem ficará por R${:.2f}'.format(dist))