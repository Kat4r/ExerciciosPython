sexo = input('Digite seu sexo, considerando M ou F: ').upper()
if sexo == 'M':               #se o input receber a letra M, então essa condição será seguida
    print('Seu sexo é masculino')
elif sexo == 'F':             #se o input receber a letra F, então essa condição será seguida
    print('Seu sexo é feminino')
else:
    print('Sexo inexistente') #se o input não receber nenhuma letra, ou uma letra incondizente, então a ultima condição será acionada

