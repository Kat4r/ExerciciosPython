import random
sorteio = 0
sorteioLista = []
print('numeros sorteados:  ( ', end='')
for i in range(0,6):
    sorteio = random.randint(1,10)
    sorteioLista.append(sorteio)
    print(str(sorteio) + ' ', end='')
print(')')

print(f'O menor numero sorteado foi: {min(sorteioLista)}')
print(f'O menor numero sorteado foi: {max(sorteioLista)}')




