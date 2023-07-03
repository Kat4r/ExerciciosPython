

def geradorMegasena(qt_jogos):
    from random import randint

    sorteio = []
    print("Gerando jogos...\n")

    for i in range(1,qt_jogos+1):
        print(f"======Aposta numero {i}=======")

        while len(sorteio) != 6:
            numAleatorio = randint(1, 60)
            if numAleatorio not in sorteio:
                sorteio.append(numAleatorio)
        print(f"{' - '.join(map(str, sorted(sorteio)))}\n")
        sorteio.clear()

geradorMegasena(5)








