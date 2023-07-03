def ajudaPy():
    from time import sleep

    print("\033[43m------------------")
    print("\033[43m  Manual AjudaPy ")
    print("\033[43m------------------")

    while True:
        razao = input("\033[mFunção ou Biblioteca: ").lower()
        if razao == "sair":
            print("\033[7:31m Finalizando sessão.")
            exit()

        print(f"\033[45m Buscando dados de {razao}")
        sleep(1)
        print("\033[7:46m")
        help(razao)

ajudaPy()



