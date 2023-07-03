import random

cores = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', ]
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis','sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um numero de 0 a 20: '))
while num < 0 or num > 20:
        num = int(input('Digite somente numeros entre 0 a 20: '))
print(random.choice(cores), f'O numero por extenso de {num} é {numeros[num]}')