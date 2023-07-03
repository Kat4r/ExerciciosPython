def cadastro():
    h18c = m1828l = c = 0

    while True:


        sexo = None

        c +=1

        print(f"====== {c}º ======")
        idade = int(input("Digite sua idade: "))
        while sexo != 'M' and sexo != 'F':
            sexo = input("Digite seu sexo [F/M]: ").strip().upper()[0]
        corCabelo = int(input("Selecione a cor de seu cabelo:\n"
                              "\033[34m[ 0 ] Castanho\n"
                              "[ 1 ] Preto\n"
                              "[ 2 ] Ruivo\n"
                              "[ 3 ] Loiro\033[m\n"
                              "Informe: "))
        if sexo == 'M' and idade >= 18 and corCabelo == 0:
            h18c += 1
        if sexo == "F" and idade >= 25 and idade <= 30 and corCabelo == 3:
            m1828l +=1

        sair = input("Deseja continuar? [S/N]: ").upper().strip()[0]
        if sair == "N":
            break

    print("foram cadastradas {} pessoas".format(c))


    if h18c:
        print("{} eram homens de cabelos castanhos com mais de 18 anos.".format(h18c))
    if m1828l:
        print("{} eram mulheres entre 25 a 30 anos com cabelos loiros.".format(m1828l))




cadastro()