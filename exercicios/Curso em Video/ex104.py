def intInput(num):

    resultado = num
    while not resultado.isdigit():
        resultado = input("\033[31mApenas numeros são aceitos!: \033[m")
    return int(resultado)

