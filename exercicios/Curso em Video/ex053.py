nome = input('Digitai: ').replace(' ', '').lower().strip()
nomeinv = nome[::-1]
if nome == nomeinv:
    print('o nome \033[32m{}\033[m é um palindromo'.format(nome))
else:
    print('O nome \033[31m{}\033[m não é um palindromo'.format(nome))


#############################

