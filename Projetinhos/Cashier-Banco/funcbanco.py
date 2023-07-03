def criarconta():
    try:
        nome = str(input('Digite seu nome: ')).strip().title()
        cpf = str(input('Digite seu cpf (sem hífen): '))
        while len(cpf) != 11 or not cpf.isdigit():
            cpf = str(input('CPF Invalido, revise os dados e digite novamente: '))

        cpfOrganizado = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]

        senhaCriada = str(input('Digite uma senha: ')).strip()
        while senhaCriada == cpf:
            print("Não use seu CPF como senha")
            senhaCriada = str(input('Tente algo mais seguro: ')).strip()
        senhaNovamente = str(input('Repita sua senha: ')).strip()

        while senhaCriada != senhaNovamente:
            print("As senhas não conferem.")
            senhaNovamente = str(input('Repita sua senha(corretamente): ')).strip()
        apelido = input('Deseja colocar usar uma alcunha em seu nome? [S/N]: ').strip().upper()[0]

        if apelido == 'S':
            apelido = input('Digite como gostaria de ser chamado(a): ').strip()
        elif apelido == 'N':
            apelido = nome

        with open('banco de dados.txt', 'a') as dados:
            dados.write('Nome: ' + nome)
            dados.write('\n')
            if apelido != nome:
                dados.write('Alcunha: ' + apelido)
                dados.write('\n')
            dados.write('CPF: ' + cpf)
            dados.write('\n')
            dados.write('Senha: ' + senhaNovamente)
            dados.write('\n')
            dados.write('------------------------')
            dados.write('\n')

        print("Dados criados!")

        return cpfOrganizado, apelido

    except Exception as e:
        print("Erro ao criar a conta:", e)

def horario():
    import datetime
    hoje = datetime.datetime.now()
    semanasLista = [0, 1, 2, 3, 4]
    diasLista = []
    for dias in range(1, 32):
        diasLista.append(dias)
    horas = hoje.hour
    minutos = hoje.minute
    horaAtual = '{:02d}:{:02d}'.format(horas, minutos)
    return horas, diasLista, horaAtual

def caixaEletronico():
    import random
    horas, diasLista, horaAtual = horario()
    notas = 0
    dia = random.choice(diasLista)
    if dia > 0 and dia <= 10:
        notas = 1800
    elif dia > 10 and dia <= 24:
        notas = 2250
    elif dia > 24:
        notas = 1200

    print('\033[4:33mAviso! Este banco está operando somente com saques de até \033[32m{}R$\033[m'.format(notas))

    saque = int(input("Valor do saque: "))
    while saque > notas:
        saque = int(input(f'\033[31mEste banco está operando somente com saques de até \033[32mR${notas}: \033[m'))
    cem = int(saque / 100)
    saque = saque - (cem * 100)
    cinquenta = int(saque / 50)
    saque = saque - (cinquenta * 50)
    vinte = int(saque / 20)
    saque = saque - (vinte * 20)
    dez = int(saque / 10)
    saque = saque - (dez * 10)
    cinco = int(saque / 5)
    saque = saque - (cinco * 5)
    dois = int(saque / 2)
    saque = saque - (dois * 2)
    if cem > 0:
        print(f'Notas de R$100: {cem}')
    if cinquenta > 0:
        print(f'Notas de R$50: {cinquenta}')
    if vinte > 0:
        print(f'Notas de R$20: {vinte}')
    if dez > 0:
        print(f'Notas de R$10: {dez}')
    if cinco > 0:
        print(f'Notas de R$5: {cinco}')
    if dois > 0:
        print(f'Notas de R$2: {dois}')

def boasvindas():
    horas = horario()[0]
    horaAtual = horario()[2]
    bemVindo = ["bom dia!", 'boa tarde!', 'boa noite']
    if horas >= 18 or horas < 5:
        print('Olá, seja bem vindo(a) ao \033[35mBig Ass Bank\033[m, tenha uma {}'.format(bemVindo[2]))
    elif horas >= 12:
        print('Olá, seja bem vindo(a) ao \033[35mBig Ass Bank\033[m, tenha uma {}'.format(bemVindo[1]))
    else:
        print('Olá, seja bem vindo(a) ao \033[35mBig Ass Bank\033[m, tenha um {}'.format(bemVindo[0]))
    print(f'\n===== Horas: \033[34m{horaAtual}\033[m ======\n')
    
def loginConta():

    bemVindo = ["bom dia!", 'boa tarde!', 'boa noite']
    horas = horario()[0]
    horaAtual = horario()[2]
    saldo = 0

    while True:
        cpf = input('Digite seu CPF (sem hífen): ')
        senha = input('Digite sua senha: ')

        with open('banco de dados.txt', 'r') as dados:
            encontrado = False
            for linha in dados:
                if linha.startswith('Nome: '):
                    nome = linha.strip().split(': ')[1]
                elif linha.startswith('Alcunha: '):
                    apelido = linha.strip().split(': ')[1]
                elif linha.startswith('CPF: '):
                    cpf_armazenado = linha.strip().split(': ')[1]
                elif linha.startswith('Senha: '):
                    senha_armazenada = linha.strip().split(': ')[1]
                elif linha.startswith('------------------------'):
                    if cpf == cpf_armazenado and senha == senha_armazenada:
                        encontrado = True
                        cpfUsar = cpf
                        senhaUsar = senha


            if not encontrado:
                print('CPF ou senha incorretos.')
            else:
                break


    with open('banco de dados.txt', 'r') as dados:
        encontrado = False
        for linha in dados:
            if linha.startswith('Nome: '):
                nome = linha.strip().split(': ')[1]
            elif linha.startswith('Alcunha: '):
                apelido = linha.strip().split(': ')[1]
            elif linha.startswith('CPF: '):
                cpf_armazenado = linha.strip().split(': ')[1]
            elif linha.startswith('Senha: '):
                senha_armazenada = linha.strip().split(': ')[1]
            elif linha.startswith('------------------------'):
                if cpfUsar == cpf_armazenado and senhaUsar == senha_armazenada:
                    encontrado = True
                    break


            nomePessoa = nome.split()[0]
            nomeSobrenome = nome.split()[1]
            nomeExibir = nomePessoa + ' ' + nomeSobrenome


    if horas >= 18 or horas < 5:
        print('Bem vindo \033[31m{}({})\033[m, tenha uma {}'.format(nomeExibir, apelido, bemVindo[2]))
    elif horas >= 12:
        print('Bem vindo \033[31m{}\033[m, tenha uma {}'.format(nomeExibir, bemVindo[1]))
    else:
        print('Bem vindo \033[31m{}\033[m, tenha um {}'.format(nomeExibir, bemVindo[0]))

    cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]

    print('='*49)
    print(f'===================== \033[34m{horaAtual}\033[m =====================')
    print('=' * 49)
    print('\033[32mNome: \033[m{}\n'
          '\033[36mCPF: \033[m{}\n'
          '\033[35mSaldo: \033[m{}\n'.format(nome,cpf,saldo))

def horariodefuncionamento():
    horas = horario()[0]
    while horas >= 23 or horas < 6:
        print('\033[31mBANCO FECHADO NO MOMENTO, \033[1:31mVOLTE MAIS TARDE!\033[0m\n'
              'Horário de funcionamento: \033[34msegunda a sexta 06:00 às 23:00\n'
              '                          sabado e domingo 09:00 às 22:00\033[m')
        exit()