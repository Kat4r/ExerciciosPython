from random import choice

def criar_forca():
    perna = '\\'
    forca = f'  ______\n' \
            f' |      |\n' \
            f' |      {"O" if vidas < 6 else ""}\n' \
            f' |     {"(" if vidas < 5 else ""}{"T" if vidas < 4 else ""}{")" if vidas < 3 else ""}\n' \
            f' |     {"/ " if vidas < 2 else ""}{perna if vidas < 1 else ""}\n' \
            f' |     \n' \
            f'=============='
    return forca

letrasUsadas = []

palavra = choice(['anfitria', 'computador', 'kocho', 'desemprego'])
vidas = 6
palavraSecreta = "_"*len(palavra)
letrasListas = list(palavraSecreta)

while vidas != 0:
    encontrado = False
    print(f'{criar_forca()}\n')
    print(f'\033[F\033[K' + f'Palavra secreta: {"".join(letrasListas)}')
    print(f'\033[F\033[K' + f'Palavra secreta: {"".join(letrasListas)}')
    chute = input("Faça seu chute: ").lower()
    while not chute.isalpha() or len(chute) != 1:
        print("Somente uma LETRA por vez. ")
        chute = input("Faça seu chute: ").lower()
    letrasUsadas.append(chute)

    for pos,letra in enumerate(palavra):
        if letra == chute:
            encontrado = True
            letrasListas[pos] = letra
    if not encontrado:
        vidas -= 1
        print(f'Vidas restantes: \033[31m{vidas}\033[m')

    if not '_' in letrasListas:
        print('\n\033[1:32mParabéns, você venceu!!\033[m')
        print(f'A palavra era \033[34m{palavra.upper()}\033[m!!\033[m')
        exit()
print('\n\033[1:31mInfelizmente você perdeu :(\n', criar_forca())












