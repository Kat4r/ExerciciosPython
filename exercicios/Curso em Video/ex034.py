sal = int(input('digite o valor atual do seu salario R$'))
if sal <= 1250:
    aumento = sal * 0.15
    nsal = aumento + sal
    print('Seu novo salario terá um aumento de 15% ({:.2f}R$) passando a ser {:.2f}'.format(aumento,nsal))
else:
    aumento = sal * 0.10
    nsal = aumento + sal
    print('Seu novo salario terá um aumento de 10% ({:.2f}R$) passando a ser {:.2f}'.format(aumento,nsal))

###############################################


