import time
nascimento = int(input('Digite o seu ano de nascimento: '))
if len(str(nascimento)) !=4:
    print('Numero digitado é invalido')
else:
    anoatual = time.localtime()
    anoatual = int(time.strftime('%Y', anoatual))
    idade = anoatual - nascimento
    if idade >= 25:
        print(' O atleta tem {} anos\n e sua classificação é MASTER'.format(idade))
    elif idade >= 18:
        print(' O atleta tem {} anos\n e sua classificação é SENIOR'.format(idade))
    elif idade >= 12:
        print(' O atleta tem {} anos\n e sua classificação é JUNIOR'.format(idade))
    elif idade >= 8:
        print(' O atleta tem {} anos\n e sua classificação é INFANTIL'.format(idade))
    elif idade >= 3:
        print(' O atleta tem {} anos\n e sua classificação é MIRIM'.format(idade))
    else:
        print(' O atleta ainda não tem idade suficiente para participar')
