km = float(input('Quantos KM foram percorridos?: '))
dia = float(input('Ha quantos dias voce o alugou?: '))
dkm = 0.15 * km
diaria = dia * 60
soma = diaria + dkm
print('Seu carro rodou {} em {} dias, portanto o aluguel sera R${}'.format(km,dia,soma))
