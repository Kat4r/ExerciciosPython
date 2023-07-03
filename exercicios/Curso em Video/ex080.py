import bisect

lista = []

for item in range(5):
    valor = input('Digite um valor: ')
    bisect.insort(lista, valor)
print(lista)


#insort em mim vai ui ui


lista = []

for item in range(5):
    valor = int(input('Digite um valor: '))

    for i in range(len(lista)):
        if valor < lista[i]:
            lista.insert(i, valor)
            print(f'item adicionado em {i+1}º lugar da lista')
            break
    else:
        lista.append(valor)
        print("item adicionado ao final da lista")


print(lista)

