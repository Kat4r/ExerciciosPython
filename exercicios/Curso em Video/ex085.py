numerais =  [[],[]]
for i in range(7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        numerais[0].append(numero)
    else:
        numerais[1].append(numero)
print(f'os numeros impares dessa lista são: {". ".join(map(str, sorted(numerais[1])))}'
      f'\nos numeros pares dessa lista são: {". ".join(map(str, sorted(numerais[0])))}')

