'''carro = input('Qual o modelo do seu carro? ').title()
if carro == 'Ferrari':
    print('SMALL COCK BRO')
elif carro == 'Lamborghini':
    print('YEA DUDE NICE COCK BRO')
else:
    print('carro medio')'''
import math

n1 = float(input('Digite sua nota em matematica '))
n2 = float(input('Digite sua nota em portugues '))

print('Sua média escolar foi {}'.format((n1+n2)/2))
if (n1+n2)/2 <= 4.9:
    print('Infelizmente voce foi reprovado')
elif (n1+n2)/2 <= 7.4:
    print('Com essa nota voce sera aprovado')
else:
    print('Parabens, sua nota foi excepcional!!'.upper())
