numeros = []
escolha = ''

while escolha != 'N':
    valorDigitado = int(input('Digite um numero: '))
    if valorDigitado not in numeros:
        numeros.append(valorDigitado)
    else:
        print('Valor digitado já se encontra na lista')
        escolha = input('Deseja continuar? [S/N]: ').upper()[0]
print(f'A ordem dos numeros digitados foram: \033[31m{sorted(numeros)}')
