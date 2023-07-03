while True:
    nome = input('Digite seu nome: ')
    if nome.isalpha():
        break
    else:
        print('O nome digitado é invalido')
while len(nome) >=8:
    print('O nome digitado é invalido!')
    nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
while idade >= 99:
    print('A idade digitada é invalida')
    idade = int(input('Digite sua idade: '))
sal = int(input('Digite seu salário: '))
while len(str(sal)) >=5:
    print()
sexo = input('Digite seu sexo: ').lower()
while sexo != 'm' and sexo != 'f':
    print('O sexo digitado está errado, revise seus dados!')
    sexo = input('Digite seu sexo: ').lower()
est_civ = input('Digite seu estado civil: ').lower()
while est_civ != 'c' and est_civ != 's':
    print('O status digitado é incorreto!')
    est_civ = input('Digite seu estado civil: ').lower()
print('\033[1:32m\nO cadastro de dados está concluido!\033[m')
