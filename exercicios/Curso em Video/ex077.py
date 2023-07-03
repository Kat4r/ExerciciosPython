palavras = ('Pneumatico',
            'Efervescencia',
            'Zoologico',
            'Perplexo',
            'Magnifico',
            'Furtivo',
            'Viscoso',
            'Plenitude',
            'Melancolico',
            'Condescendente',
            'Deslumbrante',
            'Indefinível',
            'Inevitavel',
            'Esgotado',
            'Destemido')

for palavra in palavras:
    while len(palavra) < 14:
        palavra = palavra + ' '
    letrasVogais = []
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            letrasVogais.append(letra)
    print(f'\033[31m{palavra}\033[m tem as seguintes vogais: \033[32m{(" - ".join(map(str, letrasVogais)))}\033[m')









