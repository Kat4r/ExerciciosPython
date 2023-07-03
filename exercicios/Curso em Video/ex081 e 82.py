numeros, numerosInt, pares, impares, pos5 = [], [], [], [], []
c = 0
valor = '0'

print('Digite valores aleatorios, digite qualquer letra para sair')


while valor.isdigit():
    valor = input('Digite um numero: ')
    numeros.append(valor)

numeros.pop()

for numero in numeros:
    numerosInt.append(int(numero))
numeros = numerosInt

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Foram digitados {len(numeros)} valores nessa lista')

if 5 in numeros:
    for pos, num in enumerate(numeros):
        if num == 5:
            pos5.append(pos+1)
            c += 1
    print(f'O numero 5 foi encontrado {c} vezes, nas posições {pos5}')
else:
    print('O numero 5 não foi encontrado na lista')


numeros.sort(reverse=True)
print('os valores em forma ordenada descrescente é: {}'.format(', '.join(map(str, numeros))))
print('Os pares dessa lista foram: \033[32m{}\033[m'.format(', '.join(map(str, sorted(list(set(pares)))))))
print('Os impares dessa lista foram: \033[31m{}\033[m'.format(', '.join(map(str,sorted(list(set(impares)))))))

