a1 = float(input('digite um numero: '))
a2 = float(input('digite um numero: '))
a3 = float(input('digite um numero: '))
if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
    if a1 == a2 and a1 == a3:
        print('Esses dados formam um triangulo equilatero!')
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print('os dados formam um triangulo isóceles')
    elif a1 != a2 and a1 != a3:
        print('os dados formam um triangulo escaleno!')
else:
    print('Os seguintes angulos não formam um triangulo')
