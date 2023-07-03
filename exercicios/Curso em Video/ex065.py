import numpy as np
escolha = ''
numeros = []
c = 0
while escolha != 'n':
    num = int(input('Digite um numero: '))
    escolha = input('Quer continuar? [S/N]: ').lower()[0]
    numeros.append(num)
    c += 1
num_org = np.sort(numeros)
print('O \033[32mmaior\033[m numero digitado foi {}'.format(num_org[-1]))
print('O \033[31mmenor\033[m numero digitado foi {}'.format(num_org[0]))
print('A \033[33mmédia\033[m dos valores digitados é {:.2f}'.format(sum(numeros)/c))
