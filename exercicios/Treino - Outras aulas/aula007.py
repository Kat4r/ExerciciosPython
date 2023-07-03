print('-' * 5, 'Olá', '-' * 5,)
nome = input('Vamos iniciar nossa entrevista de aumento salarial, primeiro, digite seu nome: ').capitalize()
sal = float(input('Bem vindo(a) {}, quanto você recebe atualmente? R$'.format(nome)))
if sal <= 1300:
    sal2 = sal
    aumento = sal2 * 0.2
    sal2 = aumento + sal2
    print('ótimo, pois ganhará um aumento de 20% somando ao todo R${:.2f}'.format(sal2))
    satis = input('Satisfeito com seu aumento? Digite S / N : ').strip().upper()
    if satis == 'N' or satis == 'NAO':
        aumento2 = float(input('Uma pena, gostaria então de quantos por cento em seu calculo base? '))
        if aumento2 <= 30:
            nsal = (aumento2 * sal ) / 100
            sal = nsal + sal
            print('ótimo, iremos conseguir o aumento de {}% para você'.format(aumento2))
            print('Pronto! Agora seu salario passará a ser {}'.format(sal))
        else:
            print('Infelizmente o valor fornecido está fora de nossas economias!')
    else:
        print('Que bom que está satisfeito com seu novo aumento!')
elif sal > 1300 or sal <= 1550:
    sal3 = sal
    aumento = sal3 * 0.15
    nsal = aumento + sal3
    print('ótimo, pois ganhará um aumento de 15% somando ao todo R${:.2f}'.format(nsal))
    satis = input('Satisfeito com seu aumento? Digite S / N : ').strip().upper()
    if satis == 'N' or satis == 'NAO':
        aumento2 = float(input('Uma pena, gostaria então de quantos por cento em seu calculo base? '))
        if aumento2 <= 25:
            nsal2 = (aumento2 * sal ) / 100
            sal = nsal2 + sal
            print('ótimo, iremos conseguir o aumento de {}% para você'.format(aumento2))
            print('Pronto! Agora seu salario passará a ser {}'.format(sal))
        else:
            print('Infelizmente o valor fornecido está fora de nossas economias!')
    else:
        print('Que bom que está satisfeito com seu novo aumento!')
elif sal > 1550:
    sal4 = sal
    aumento = sal4 * 0.1
    nsal = aumento + sal4
    print('ótimo, pois ganhará um aumento de 15% somando ao todo R${:.2f}'.format(nsal))
    satis = input('Satisfeito com seu aumento? Digite S / N : ').strip().upper()
    if satis == 'N' or satis == 'NAO':
        aumento2 = float(input('Uma pena, gostaria então de quantos por cento em seu calculo base? '))
        if aumento2 <= 20:
            nsal = (aumento2 * sal ) / 100
            sal = nsal + sal
            print('ótimo, iremos conseguir o aumento de {}% para você'.format(aumento2))
            print('Pronto! Agora seu salario passará a ser {}'.format(sal))
        else:
            print('Infelizmente o valor fornecido está fora de nossas economias!')
    else:
        print('Que bom que está satisfeito com seu novo aumento!')
else:
    print('Valor invalido! tente novamente.')



