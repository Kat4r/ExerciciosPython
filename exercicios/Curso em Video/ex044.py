prod = int(input('Digite o preço do produto: ')).__abs__()
if prod <= 150:
    print('Desculpe, não parcelamos valores inferiores a R$150')
    print('Mas oferecemos até 10% de desconto para pagamento a vista')
    escolha = int(input('Escolha a forma de pagamento desejada:'
                        '\n\033[1:33m[ 0 ] A vista'
                        '\n[ 1 ] A vista no cartão\033[m'
                        '\ndigite sua escolha:'))
    if escolha == 0:
        desc = (prod * 10) / 100
        print('Pagando a vista você ganhará um desconto de 10%!\nficando por apenas \033[1:32mR${:.2f}\033[m!'.format(
            prod - desc))
    elif escolha == 1:
        desc = (prod * 5) / 100
        print('Pagando a vista você ganhará um desconto de 5%!\nficando por apenas \033[1:32mR${:.2f}\033[m!!'.format(
            prod - desc))
else:
    escolha = int(input('Escolha a forma de pagamento desejada:'
                        '\n\033[1:33m[ 0 ] A vista'
                        '\n[ 1 ] A vista no cartão'
                        '\n[ 2 ] parcelado em 2x'
                        '\n[ 3 ] parcelado em 3x ou mais\033[m'
                        '\ndigite sua escolha: '))
    if escolha == 0:
        desc = (prod * 10) / 100
        print('Pagando a vista você ganhará um desconto de 10%!\nficando por apenas \033[1:32mR${:.2f}\033[m!'.format(
            prod - desc))
    elif escolha == 1:
        desc = (prod * 5) / 100
        print('Pagando a vista você ganhará um desconto de 5%!\nficando por apenas \033[1:32mR${:.2f}\033[m!!'.format(
            prod - desc))
    elif escolha == 2:
        print(
            'Parcelando em 2X \033[1:33mnão haverá descontos\033[m, ficando o preço normal, cada parcela será de \033[1:32mR${:.2f}\033[m'.format(
                prod / 2))
    elif escolha == 3:
        parc = int(input('Deseja parcelar em quantas vezes? \033[1:32mlimite = 12:\033[m '))
        if parc > 12:
            print('Não há como parcelar em mais de 12 vezes.')
        elif parc == 2:
            print(
                'Parcelando em 2X \033[1:33mnão haverá descontos\033[m, ficando o preço normal, cada parcela será de \033[1:32mR${:.2f}\033[m'.format(
                    prod / 2))
        elif parc == 1:
            desc = (prod * 5) / 100
            print(
                'Pagando a vista você ganhará um desconto de 5%!\nficando por apenas \033[1:32mR${:.2f}\033[m!!'.format(
                    prod - desc))
        else:
            juros = (prod * 20) / 100
            mes = prod + juros
            mes2 = mes / parc
            print(
                'Com esse metodo de pagamento, seu produto terá um \033[31maumento de 20%\033[m, sendo um total de {:.2f} por \033[34m{}\033[m parcelas'.format(
                    mes2, parc))
            print('Seu produto custará \033[31mR${:.2f}\033[m no final do pagamento'.format(mes))
    else:
        print('\033[31mEscolha invalida.')
