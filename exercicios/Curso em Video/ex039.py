sex = input('Digite seu sexo, considerando M ou F: ').upper()
if sex == "M":
    nascimento = int(input('Digite seu ano de nascimento: '))
    idade = 2023 - nascimento
    if idade == 18:
        print('Quem nasceu em {} terá 18 anos esse ano! portando poderá ser \033[32malistado!'.format(nascimento))
    elif idade < 18:
        print('Você ainda não tem 18 anos, seu alistamento sera somente daqui {} anos'.format(18 - idade))
        print('Portanto seu alistamento será em {}'.format(nascimento + 18))
    elif idade > 18:
        print('Você deveria ter se alistado ha {} anos '.format(idade - 18))
        print('Seu alistamento foi em {}'.format(nascimento + 19))
else:
    print('O alistamento obrigatorio é somente para homens')











