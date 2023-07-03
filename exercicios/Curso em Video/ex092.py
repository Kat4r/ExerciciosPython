import datetime

anoAtual = datetime.datetime.now().year

cadastro = {}

while True:

    cadastro['Nome'] = input("Digite seu nome: ").strip().title()

    cadastro['Ano de nascimento'] = 0
    while cadastro['Ano de nascimento'] > anoAtual or cadastro['Ano de nascimento'] < 1900:
        cadastro['Ano de nascimento'] = int(input("Digite o ano em que você nasceu: "))

    cadastro['Carteira de Trabalho'] = int(input("Digite sua CTPS \033[31m[ 0 ]\033[m se não tiver: "))
    if cadastro['Carteira de Trabalho'] == 0:
        print("\n-------------------------")
        break

    cadastro['Ano de contratação'] = 0
    while cadastro['Ano de contratação'] < cadastro['Ano de nascimento'] or cadastro['Ano de contratação'] > anoAtual:
        cadastro['Ano de contratação'] = int(input("Digite o ano de sua contratação: "))

    cadastro['Salário R$'] = int(input("Digite seu salario R$"))
    print("\n-------------------------")
    break

for info, dado in list(cadastro.items()):
    if dado == 0:
        pass
    else:
        print(f"{info}: {dado}")

if cadastro['Carteira de Trabalho'] > 0:
    print(f"Você irá se aposentar em: {cadastro['Ano de contratação'] + 35}")








