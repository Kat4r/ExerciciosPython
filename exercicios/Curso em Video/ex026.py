nome = str(input('Digite seu nome: ')).strip().lower()
print('Olá {}'.format(nome.title()))
print('Seu nome contem {} letras A'.format(nome.count('a')))
print('ela aparece na posição {} pela primeira vez'.format(nome.find('a') + 1))
print('ela aparece na posição {} pela ultima vez'.format(nome.rfind('a') + 1))
print('sinceramente viu...')

