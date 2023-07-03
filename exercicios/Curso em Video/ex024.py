cidade = str(input('digite o nome de sua cidade: ')).strip().title()
print('A cidade começa com santo? {}'.format(cidade[:6] == 'Santo '))