def geradorSenha():
    import string
    from random import choice
    seg_baixa = string.ascii_letters + string.digits.strip()
    seg_media = string.ascii_letters + string.punctuation.strip()
    seg_alta = string.printable.strip()

    while True:
        escolha = int(input(
            'Escolha um nivel de segurança\n [ 1 ] Nível de segurança Básico\n [ 2 ] Nível de segurança Médio\n [ 3 ] Nível de segurança Avançado\n Escolha: '))
        if escolha == 1:
            valores = seg_baixa
            break
        elif escolha == 2:
            valores = seg_media
            break
        elif escolha == 3:
            valores = seg_alta
            break
        else:
            print('Digite um número válido.')

    tamanhosenha = ''
    while True:
        tamanho = int(input('Escolha o tamanho da senha [ 4 - 24 ]: '))
        if tamanho >= 4 and tamanho <= 24:
            break
        else:
            print('Digite um número válido')
    for i in range(tamanho):
        tamanhosenha += choice(valores)
    senha = tamanhosenha
    return senha


def cadastrarUsuario():

    usuario = input('Digite o nome do usuario: ')
    criar_senha = str(input('[ 1 ] Crie sua própria senha.\n[ 2 ] Gere uma senha aleatória. \n Escolha: '))


    if criar_senha == '1':
        senha = input('Digite sua senha: ')
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write('\n' + 'User: ' + usuario + '\n' + 'Senha: ' + senha + '\n')
            arquivo.write('------------')
            return senha


    elif criar_senha == '2':
        senha = geradorSenha()
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write('\n' + 'User: ' + usuario + '\n' + 'Senha: ' + senha + '\n')
            arquivo.write('------------')
            return senha

    print('Usuario criado com sucesso!')
    return usuario


def fazerLogin():


    while True:
        usuario = input('Digite o nome do usuario: ')
        senha = input('Digite a senha: ')
        with open('usuarios.txt', 'r') as arquivo:
            login = False
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.startswith('User: '):
                    usuarioArmazenado = linha.strip().split(': ')[1]
                elif linha.startswith('Senha: '):
                    senhaArmazenada = linha.strip().split(': ')[1]
                elif linha.startswith('------------'):
                    if senha == senhaArmazenada and usuario == usuarioArmazenado:
                        login = True


            if not login:
                print('Dados invalidos')
            else:
                print("Login realizado com sucesso!")
                break





