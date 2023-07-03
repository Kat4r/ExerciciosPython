saque = float(input('Digite o valor do saque \033[32mR$\033[m'))
cem = int(saque / 100)
saque = saque - (cem * 100)
cinquenta = int(saque / 50)
saque = saque - (cinquenta * 50)
vinte = int(saque / 20)
saque = saque - (vinte * 20)
dez = int(saque / 10)
saque = saque - (dez * 10)
cinco = int(saque / 5)
saque = saque - (cinco * 5)
um = int(saque)


print(f'seu saque terá: \n'
      f'{cem}\033[36m notas de 100\033[m \n'
      f'{cinquenta}\033[33m notas de 50\033[m \n'
      f'{vinte}\033[33m notas de 20\033[m \n'
      f'{dez}\033[35m notas de 10\033[m \n'
      f'{cinco}\033[35m notas de 5\033[m \n'
      f'{um}\033[32m notas de 1\033[m \n')

