pessoas, info, magreza, gordura = [], [], [], []
menorValor = float('inf')
maiorValor = 0


for c in range(0,int(input('Quantas pessoas dejesa cadastrar?: '))):
    c += 1
    print('----{}º Pessoa----'.format(c))
    info.append(input('Digite seu nome: '))
    info.append(int(input('Digite seu peso: ')))
    pessoas.append(info[:])
    info.clear()

for pessoa in pessoas:
    if pessoa[1] < menorValor:
        menorValor = pessoa[1]
        magreza.append(menorValor)

    elif pessoa[1] > maiorValor:
        maiorValor = pessoa[1]
        gordura.append(maiorValor)

print(magreza, gordura, pessoas)








