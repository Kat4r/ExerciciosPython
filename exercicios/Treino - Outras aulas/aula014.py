n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

lista = [n1,n2]
soma = 0
for num in lista:   #para cada numero na lista é somado em ordem de adição
    soma = soma + num
    while soma > num:   #while usado pra saber quando a soma for maior que os numeros usados na lista
        soma = soma / len(lista) #a soma total é divida pelo tanto de item que tiver na lista + break pro loop se encerrar
        break
print('a media entra os numeros {} e {} é {}.'.format(lista[0],lista[1],int(soma)))


'''Escreva um programa que leia uma lista de números e imprima a média dos valores da lista.'''