from modulos.banco.funcoes import *
from modulos.banco.objetos import *

horariofuncionamento()

interface()

opcao = 0
while opcao <1 or opcao > 3:
    try:
        opcao = int(input("O que você deseja? \n\n"
                          "[ 1 ] Acessar Conta\n"
                          "[ 2 ] Criar Conta\n"
                          "[ 3 ] Sair\n\n"
                          "Responda aqui: "))

        if opcao == 1:
            pass
        elif opcao == 2:
            nome = input("Digite seu nome: ").strip().title()
            saldoIni = int(input("Saldo inicial: "))
            limite = ''
            while not limite.isdigit():
                limite = converterLimite(input("Limite de conta \033[33m[Vazio se não houver]\033[m:"))
        elif opcao == 3:
            print("Volte sempre!")
            exit()


    except Exception as erro:
        print(erro)


