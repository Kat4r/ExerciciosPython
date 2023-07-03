n1 = int(input('DIgite um numero: '))
n2 = int(input('DIgite outro numero: '))
n3 = int(input('DIgite outro numero: '))
if n1 < n2:               #testa se o primeiro numero é menor que o segundo
    n1,n2 = n2,n1         #se sim, o segundo numero passa a ocupar a casa do primeiro
if n1 < n3:               #testa se o primeiro numero é menor que o terceiro
    n1,n3 = n3,n1         #se sim, o primeiro numero passa a ocupar a casa do primeiro, se tornando o numero de mais ALTO valor
if n2 < n3:               #por fim verifica se o segundo numero é menor que o ultimo
    n2,n3 = n3,n2         #se sim, suas casas sao invertidas, tornando N3 o numero de menor valor

print('os numeros digitados em ordem decrescente serão: {} {} {}'.format(n1,n2,n3))

"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""
