from modulos import cadastroBase as login
from modulos.libtestes import testespy as tpy

pasta = "Cadastro.txt"
login.abertura()
login.menu(["Cadastrar pessoas", "Mostrar pessoas cadastradas", "Sair"])
opcoes = 4

while opcoes != 3:
    try:
        opcoes = int(input("\nInforme a seguir a opção desejada: "))
        while opcoes < 1 or opcoes > 3:
            opcoes = int(input("\033[31mERRO: Digite apenas os numeros de\033[32m1 a 3\033[m: "))

        if opcoes == 1:
            login.intro(opcoes)
            login.cadastro(tpy.nomesRand(tpy.choice(["f", "m"])), str(tpy.idadeRand()), pasta)
        elif opcoes == 2:
            login.intro(opcoes)
            login.mostrarCadastro(pasta)

    except:
        print("\033[31mERRO: Digite somente numeros inteiros de \033[32m1 a 3\033[m: ")
        continue

print("\033[34mFinalizando a execução do programa. . . ")


