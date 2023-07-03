lista, posMaior, posMenor = [], [], []
menorValor = float('inf')
maiorValor = 0

for i in range(0,5):
    num = int(input('Digite um numero: '))
    lista.append(num)

for pos,valor in enumerate(lista):
    if valor < menorValor:
        menorValor = valor
        posMenor = [pos]
    elif valor == menorValor:
        posMenor.append(pos)
    if valor > maiorValor:
        maiorValor = valor
        posMaior = [pos]
    elif valor == maiorValor:
        posMenor.append(pos)


print(f'O menor numero encontrado na lista foi: {menorValor} na posição: {posMenor}')
print(f'O maior valor encontrado na lista foi: {maiorValor} na posição: {posMaior}')

















