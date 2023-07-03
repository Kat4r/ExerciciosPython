#minha versao

nome = input('digite seu nome completo: ')
lista = nome.split()
sep = len(nome.replace(' ',''))
print('seu nome em caixa alta ficará: {}'.format(nome.upper()))
print('seu nome em em caixa baixa ficará: {}'.format(nome.lower()))
print('seu nome com letras iniciais em maiusculo ficará: {}'.format(nome.title()))
print('seu nome contem ao todo {} letras'.format(len(nome.replace(' ',''))))
print('seu primeiro nome contem apenas {} letras'.format(len(lista[1])))

#versao do professor

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa =nome.split()
print('Seu primeiro nome é {} e  ele tem {} letras'.format(separa[0], len(separa[0])))