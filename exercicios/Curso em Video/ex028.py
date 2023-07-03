import random
num = int(input('Digite um numero de 0 a 5: '))
esc = random.randrange(6)
if esc == num:
    print('Parabens, voce acertou!! a escolha realmente foi {}'.format(num))
else:
    print('Haha! Você errou, minha escolha foi {}'.format(esc))