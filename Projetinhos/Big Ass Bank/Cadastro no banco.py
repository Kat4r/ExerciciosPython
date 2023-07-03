import funcbanco

funcbanco.horariodefuncionamento()
funcbanco.boasvindas()

print('Deseja entrar em uma conta já cadastrada ou criar uma nova?')
escolha = str(input('            [ 0 ] \033[32mCriar\033[m nova conta\n'
                    '            [ 1 ] \033[1:33mEntrar\033[m em conta\n'
                    'Digite sua escolha referente as opções: '))[0]
while escolha not in ('0', '1'):
    escolha = input(('Digite sua escolha referente as opções \033[31m0\033[m e \033[31m1\033[m: ') + '\n' * 2)[0]


if escolha == '0':
    funcbanco.criarconta()
    continuar = input('Deseja acessar sua conta? [S/N]').strip().upper()[0]
    while continuar not in ('S', 'N'):
        continuar = input('Use somente S ou N: ').strip().upper()[0]
        if continuar == 'S':
            funcbanco.loginConta()





elif escolha == '1':
    funcbanco.loginConta()

