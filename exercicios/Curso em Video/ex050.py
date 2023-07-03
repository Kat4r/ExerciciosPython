soma = 0
for num in range(0,6):
    par = int(input('Digite um numero: '))
    if par % 2 == 0:
        soma = soma + par
print('A soma entre os numeros citados é {}'.format(soma))
