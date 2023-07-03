cont = soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print('A soma entre os {} numeros somados equivale a {}'.format(cont, soma))
