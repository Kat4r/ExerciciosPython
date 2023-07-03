def tentoone():

    import time
    escolha = 0
    numeros = [[],[]]
    while escolha != 2:
        print("="*19)
        print("="*6,'MENU',"="*7)
        print("=" * 19)
        print("| [ 0 ] de 1 a 10 |")
        print("| [ 1 ] de 10 a 1 |")
        print("| [ 2 ] para Sair |")
        print("=" * 19)
        escolha = int(input("Digite um numero [0 a 2]: "))
        while escolha <0 or escolha >2:
            escolha = int(input("Digite apenas os seguintes numeros [0 a 2]: "))

        if escolha == 0:
            for i in range(0,11):
                numeros[0].append(i)
            print(", ".join(map(str, numeros[0])))


        elif escolha == 1:
            for i in range(10,-1,-1):
                numeros[1].append(i)
            print(", ".join(map(str, numeros[1])))

        else:
            exit()

        time.sleep(5)
        print("\n"*5)

tentoone()