from random import choice, randint
from datetime import datetime as ano


def nomesRand(sexo):

    if sexo == "m":
        with open("H:\\Meus Códigos\\paito\\ai ui ai ui q dor\\modulos\\libtestes\\amigosH.txt", "r", encoding="utf-8") as homens:
            homens = [i.strip().title() for i in homens]
            nome = choice(homens)
            return nome

    else:
        with open("H:\\Meus Códigos\\paito\\ai ui ai ui q dor\\modulos\\libtestes\\amigosM.txt", "r", encoding="utf-8") as mulheres:
            mulheres = [i.strip().title() for i in mulheres]
            nome = choice(mulheres)
            return nome

def nomesJogadoresRand():
    with open("H:\\Meus Códigos\\paito\\ai ui ai ui q dor\\modulos\\libtestes\\jogadores.txt", "r", encoding="utf-8") as jogadores:
        jogadores = [i.strip() for i in jogadores]
        jogador = choice(jogadores)
        return jogador

def itensRand():
    with open("H:\\Meus Códigos\\paito\\ai ui ai ui q dor\\modulos\\libtestes\\itens.txt", "r", encoding="utf-8") as itens:
        itens = [i.strip() for i in itens]
        item = choice(itens)
        return item

def idadeRand():
    anoAtual = ano.now().year
    idadeGerada = float('inf')
    while idadeGerada >= anoAtual:
        idadeGerada = randint(12, 100)
    return idadeGerada

def timesRand():
    with open("H:\\Meus Códigos\\paito\\ai ui ai ui q dor\\modulos\\libtestes\\times.txt", "r", encoding="utf-8") as times:
        times = [i.strip() for i in times]
        time = choice(times)
        return time

def fibonacci(n_termos):
    """
    Na matemática, a sucessão de Fibonacci (ou sequência de Fibonacci), é uma sequência de números inteiros,
    começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores.

    :param n_termos: termos a serem mostrados em uma sequencia de fibonacci
    :return:
    """
    antes = ultimo = 1
    soma = []
    c = 0

    if n_termos == 1:
        print('\033[31m', '1')
    elif n_termos == 0:
        print('Esse numero não possui sequencia de fibonacci')
    else:
        print('\033[31m', '1   1', end='  ')
        while n_termos > 1:
            termo_atual = ultimo + antes
            antes = ultimo
            ultimo = termo_atual
            print('\033[31m', termo_atual, '\033[m', end=' ')
            n_termos -= 1
            c += 1
            soma.append(termo_atual)
        print('\nesses são os \033[32m{}-ésimos\033[m termos da Fibonacci'.format(c + 1))
        print('A soma dos termos apresentados nessa Fibonacci equivalem a \033[4:36m{}'.format(sum(soma) + 1))

def fatorial(num, show=False):
    """
    Calculadora de fatoriais

    :param num: Recebe um numero que é feita a conta fatorial
    :param show: variavel booleana de True ou False, serve somente para ignorar ou não a conta feita
    """

    num_lista = []
    soma = 1
    for i in range(num, 1, -1):
        num_lista.append(i)

    if show:
        for numeros in num_lista:
            print(f"x {numeros}", end=" ")
            soma = soma * numeros
        return f"= {soma}"

    else:
        for numeros in num_lista:
            soma = soma * numeros
        return soma

def geradorMegasena(qt_jogos):
    from random import randint

    sorteio = []
    print("Gerando jogos...\n")

    for i in range(1, qt_jogos + 1):
        print(f"======Aposta numero {i}=======")

        while len(sorteio) != 6:
            numAleatorio = randint(1, 60)
            if numAleatorio not in sorteio:
                sorteio.append(numAleatorio)
        print(f"{' - '.join(map(str, sorted(sorteio)))}\n")
        sorteio.clear()

def carrosRand():
    with open("H:\\Meus Códigos\\paito\\ai ui ai ui q dor\\modulos\\libtestes\\carros.txt", 'r', encoding='utf-8') as carros:
        carros = [i.split() for i in carros]
        carro = choice(carros)
        carro = ' '.join(carro)
        return carro

def intInput(num):
    resultado = num
    while not resultado.isdigit():
        resultado = input("\033[31mApenas numeros são aceitos!: \033[m")
    return int(resultado)

def encontrarMassa(lista, gordo=False):
    posMaior = posMenor = maiorPeso = menorPeso = 0

    for pos, peso in enumerate(lista):
        if pos == 0:
            maiorPeso = menorPeso = peso
        if peso > maiorPeso:
            maiorPeso = peso
            posMaior = pos
        if peso < menorPeso:
            menorPeso = peso
            posMenor = pos

    return posMaior if gordo else posMenor