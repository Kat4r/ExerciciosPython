notacorte = input('Digite a nota de 2 materias separadamente: ').split()
nota = ''
result = ''
if len(notacorte) >= 3:
    print('\033[41mNumeros informados não correspondem as expectativas do programa\033[m')
else:
    notacorte = float(notacorte[0]), float(notacorte[1])
    soma = (notacorte[0] + notacorte[1]) / 2
    if notacorte[0] >10 or notacorte[1] >10:
        print('numeros informados excedem o limite de \033[1:31m10!')
    else:
        if soma > 9 and soma == 10:
            nota = "A"
            result = 'aprovado'
        if soma > 7.5 and soma <= 9:
            nota = 'B'
            result = 'aprovado'
        if soma > 6 and soma <= 7.5:
            nota = 'C'
            result = 'para a recuperação'
        if soma > 4 and soma <= 6:
            nota = 'D'
            result = 'reprovado'
        if soma < 4:
            nota = "E"
            result = 'reprovado'
        print('Sua média final foi \033[32m{}\033[m então você foi \033[33m{}\033[m'.format(nota, result.upper()))

