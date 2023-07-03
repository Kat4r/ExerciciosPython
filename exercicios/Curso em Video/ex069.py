quant = mais18 = h = m = m_nova = 0
continuar = ''
while True:
    sexo = ''
    idade = 0
    quant += 1
    print('---|{}* Pessoa|---'.format(quant))
    while idade > 99 or idade <= 0:
        idade = int(input('Digite sua idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite seu Sexo [M/F]: ')).upper()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m_nova += 1
    continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {quant} pessoas;'
      f' dentre elas há {mais18} pessoas com mais de 18 anos, '
      f'{h} homens e {m_nova} mulheres com menos de 20 anos')


