numero = int(input('digite um numero de  o a 9999: '))
unidade = numero % 10
numero = (numero - unidade)/10
dez = numero %10
numero = (numero - dez)/10
cen = numero %10
numero = (numero - cen)/10
mil = numero %10
print('seu numero tem {} unidades'.format(int(unidade)))
print('{} dezenas'.format(int(dez)))
print('{} centenas'.format(int(cen)))
print('{} milhares'.format(int(mil)))