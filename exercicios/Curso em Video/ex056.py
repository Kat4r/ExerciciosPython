sexo = input('Digite seu sexo \033[33m[M/F]\033[m : ').lower()
while sexo != 'm' and sexo != 'f':
    sexo = input('Sexo digitado é invalido, \033[31mpor favcr revise os dados!\033[m: ')
if sexo == 'm':
    print('\033[35mDados MASCULINOS registrados')
else:
    print('\033[34mDados FEMININOS registrados')