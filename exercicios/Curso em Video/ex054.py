import time
anoatual = time.localtime()
anoatual = int(time.strftime('%Y', anoatual))
idademaior = idademenor = nascimento = frase = 0
for frase in range(0,6):
    nascimento = int(input("digite a {}º idade: ".format(frase+1)))
    idade = anoatual - nascimento
    while len(str(nascimento)) != 4 or nascimento > anoatual or nascimento < 1900:
        nascimento = int(input("Digite a idade corretamente! "))
    if idade >= 18:
        idademaior = idademaior + 1
    else:
        idademenor = idademenor + 1
print('Há \033[1:33m{}\033[m pessoas de \033[1:32mmaioridade\033[m nessa lista'.format(idademaior))
print('Há \033[1:33m{}\033[m pessoas de \033[1:31mmenoridade\033[m nessa lista'.format(idademenor))

