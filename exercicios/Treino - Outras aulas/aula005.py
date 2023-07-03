p1 = int(input('Diga o preço do produto x: '))
p2 = int(input('Diga o preço do produto y: '))
p3 = int(input('Diga o preço do produto z: '))
if p1 < p2 and p1 < p3:
    print('O produto mais barato é o X por R${:.2f}'.format(p1))
elif p2 < p1 and p2 < p3:
    print('O produto mais barato é o Y R${:.2f}'.format(p2))
else:
    print('O produto mais barato é o Z R${:.2f}'.format(p3))
