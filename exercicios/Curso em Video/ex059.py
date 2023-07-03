pessoas = idades = []
idade = maior = c = 0
sexo = homemvelho = ''

for i in range(1,5):
    print('----- {}° PESSOA -----'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    idades.append(idade)
    sexo = input('Sexo: ').upper()
    while sexo != 'M' and sexo != 'F':
        print('\033[31mSexo invalido!\033[m')
        sexo = input('Digite novamente: ').upper()
    if sexo == 'M' and idade > maior:
        maior = idade
        homemvelho = nome
    if sexo == 'F' and idade <= 20:
        c = c + 1
print('A média de idade desse grupo é \033[35m{}\033[m'.format(sum(idades) /4))
if sexo == 'M':
    print('O homem mais velho desse grupo é o \033[33m{}\033[m'.format(homemvelho.title()))
else:
    print('Não há homens no grupo')
if sexo == 'F' and c >= 1:
    print('há \033[32m{}\033[m garotas com menos de 20 anos no grupo'.format(c))
